# HTTP and Application Server
.fx: title

__CS290B__

Dr. Bryce Boe

October 8, 2015

---

# Today's Agenda

* TODO
* HTTP Server Architectures
* C10K Problem
* Application Servers

---

# TODO

## Should be done

* Ruby Codecademy
* Agile Web Development with Rails Chapters 1 through 8
* Familiarity with Git (you'll get more practice)

## Before Tuesday's Class:

* [Dynamic Load Balancing on Web-server Systems](http://www.ics.uci.edu/~cs230/reading/DLB.pdf)
  by Cardellini, Colajanni, and Yu.

## By End of Today's Lab:

* Add member names and photo to project's README on github
* Create team project on pivotal tracker and add me (bryce.boe@appfolio.com) as
  me as collaborator

---

# HTTP Server Architectures

* Single Threaded (no concurrency)
* Process per request
* Process pool
* Thread per request
* Process/thread worker pool
* Event-driven

---

# Single Threaded HTTP Servers

    bind() to port 80 and listen()
    loop forever
        accept() a socket connection
        while we can read from the socket
            read() a request
            process that request
            write() its response
        close() the socket connection

> If another request comes in while we're within the loop what happens?

---

# Single Threaded Problem

If a single threaded web service does not process the request quickly, other
clients end up waiting or dropping their connections.

We are building web application not web sites. As a result:

* The requests are usually more complicated than serving a file from disk.
* It is common to have a web request doing a significant amount of computation
  and business logic.
* It is common to have a web request result in connections to multiple external
  services, e.g., databases, and caching stores
* These requests can be anything: lightweight or heavyweight, IO intensive or
  CPU intensive

We can solve these problems if the thread of control that processes the request
is separate from the thread that `listen()`s and `accept()`s new connections.

---

# Process per Request HTTP Server

Handle each request as a subprocess:

.fx: img-left

![forking web server](img/server_forking.png)

    bind() to port 80 and listen()
    loop forever
        accept() a socket connection
        if fork() == 0  # child process
            while we can read from the socket
                read() a request
                process that request
                write() its response
            close() the socket connection
            exit()

---

# Process per Request HTTP Server

## Strengths

* Simple
* Provides easy isolation between requests
* No threading issues

## Weaknesses

* Does each request duplicate the process memory?
* What happens as the CPU load increases?
* How efficient is it to fire up a process on each request?
    * How much setup and teardown work is necessary?

---

# Process Pool HTTP Server

.fx: img-left

![process pool web server](img/server_process_pool.png)

Instead of spawning a process for each request create a pool of N processes at
start-up and have them handle incoming requests when available.

The children processes `accept()` the incoming connections and use shared
memory to coordinate.

The parent process watches the load on its children and can adjust the pool
size as needed.

---

# Process Pool HTTP Server

## Strengths

* Provides easy isolation between requests
* Children can die after _M_ requests to avoid memory leakage
* Process setup and teardown costs are minimized
* More predictable behavior under high load
* No threading issues

## Weaknesses

* More complex than process per request
* Many processes can still mean a large amount of memory consumption

This web server architecture is provded by the Apache 2.x MPM "Prefork" module.

---

# Thread per Request HTTP Server

Why use multiple processes at all? Instead we can use a single process and
spawn new threads for each request.

.fx: img-left

![http server thread per request](img/server_threaded.png)

    bind() to port 80 and listen()
    loop forever
        accept() a socket connection
        pthread_create()  # function that...
            while we can read from the socket
                read() a request
                process that request
                write() its response
            close() the socket connection
            # thread dies


---

# Thread per Request HTTP Server

## Strengths

* Relatively simple
* Reduced memory footprint compared to multi-processed

## Weaknesses

* Request handling code must be thread-safe
* Pushing thread-safety to the application developer is not ideal
* Setup and tear down needs to occur for each thread (or shared data
  needs to be thread-safe)
* Memory leaks?

---

# Process/Thread Worker Pool Server

.fx: img-left

![http process/thread worker pool](img/server_worker_pool.png)

Combination of the two techniques.

Master process spawns processes, each with many threads. Master maintains
process pool.

Processes coordinate through shared memory to `accept()` requests.

Fixed threads per request, scaling is done at the process level.

---

# Process/Thread Worker Pool Server

## Strengths

* Faults isolated between processes, but not threads
* Threads reduce memory footprint
* Tunable level of isolation
* Controlling the number of processes and threads allows for predictable
  behavior under load

## Weaknesses

* Requires thread-safe code
* Uses more meory than an all-thread based approach

This web server architecture is provded by the Apache 2.x MPM "Worker" module.


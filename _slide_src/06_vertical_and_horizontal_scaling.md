# Vertical and Horizontal Scaling
.fx: title

__CS290B__

Dr. Bryce Boe

October 13, 2015

---

# Today's Agenda

* TODO
* Server Architecture Review
* Motivation
* Vertical Scaling
* Horizontal Scaling

---

# TODO

## Should be done

* Ruby Codecademy
* Agile Web Development with Rails Chapters 1 through 8
* Familiarity with Git (you'll get more practice)
* [Dynamic Load Balancing on Web-server Systems](http://www.ics.uci.edu/~cs230/reading/DLB.pdf)
  by Cardellini, Colajanni, and Yu.
* Pivotal contains stories for the entire project
* Github contains base-rails app (and more)

## Before Lab

* Agile Web Development with Rails Chapters 9 through 17
* Make as much progress on Sprint 1 commitment as possible

__Focus__: On delivering new usable features to your customers (Seb and me) for
the next few weeks.

---

# HTTP Server Architectures

* Single Threaded (no concurrency)
* Process per request
* Process pool
* Thread per request
* Process/thread worker pool
* Event-driven

---

# What are the trade-offs of process-based concurrency?

---

# What are the trade-offs of thread-based concurrency?

---

# What are the trade-offs of event-driven systems?

---

# Scaling Goal

![Load Balanced Topology](img/load_balanced_topology.png)

After today you will understand what load balancing is, and why the depicted
architecture provides smooth cost-effective scaling.

---

# The Problem

You've built something the world (or significant subset) is excited about.

> What do you do when your popularity doubles (again, and again)?

---

# The Solutions

## Vertical Scaling

Buying "bigger" hardware and scaling _up_

* __PRO__: Easy
* __CON__: Limited
* __CON__: Non-linear increase in cost when scaling

## Horizontal Scaling

Buying move servers and scaling _out_

* __PRO__: Easy to add more servers (limited by data center space)
* __PRO__: Linear increase in cost when scaling
* __CON__: More moving parts makes things more complicated

---

# Vertical Scaling

When needed, increase the resources of your current server, eventually buy a
bigger server with:

* More memory
* More and/or faster CPUs and/or cores
* Higher bandwidth

---

## EC2 and Vertical Scaling

With Amazon EC2 you rent virtual instances. There are clear vertical scaling
paths. Each type of instance (below) has a few options ranging from lower
resources/performance to higher resources/performance:

* __T__ and __M__ prefixed instances: balanced mix of memory and CPU
* __C__ prefixed instances: CPU optimized
* __R__ prefixed instances: Memory optimized
* __G__ prefixed instances: GPU optimized
* __I__ prefixed instances: I/O optimized
* __D__ prefixed instances: Storage capacity optimized

---

# Scaling Test: Simulated Users

We will use the same test setup explained in the last lecture.

Using Tsung (erlang-based test framework) we will simulate multiple users
visiting the Demo App web service. Each user will:

    Visit the homepage (/)
      Wait randomly between 0 and 2 seconds
    Request community creation form
      Wait randomly between 0 and 2 seconds
    Submit new community form
    Request new link submission form
      Wait randomly between 0 and 2 seconds
    Submit new link submission form
      Wait randomly between 0 and 2 seconds
    Delete the link
      Wait randomly between 0 and 2 seconds
    Delete the community

---

# Scaling Test: Phases

This time we have twelve phases of testing each lasting 60 seconds:

     1.    (0-59s) Every second a new simulated user arrives
     2.  (60-119s) Every second 1.5 new simulated users arrive
     3. (120-179s) Every second 2 new simulated users arrive
     4. (180-239s) Every second 4 new simulated users arrive
     5. (240-299s) Every second 6 new simulated users arrive
     6. (300-359s) Every second 10 new simulated users arrive
     7. (360-419s) Every second 16 new simulated users arrive
     8. (420-479s) Every second 20 new simulated users arrive
     9. (480-539s) Every second 25 new simulated users arrive
    10. (540-599s) Every second 35 new simulated users arrive
    11. (600-659s) Every second 45 new simulated users arrive
    12. (660-719s) Every second 55 new simulated users arrive

---

# Vertical Scaling: M3 Large Instance

.fx: img-left

![M3 Large Instance Graph](img/vertical_scaling_m3_large.png)

* 2 vCPUs
* 7.5 GB Memory
* SSD storage
* $100 per month

Handles 6 new users per second (ups).

Fails with 10 ups.

---

# Vertical Scaling: M3 X-Large Instance

.fx: img-left

![M3 X-Large Instance Graph](img/vertical_scaling_m3_xlarge.png)

* 4 vCPUs
* 15 GB Memory
* SSD storage
* $200 per month

Handles 10 new users per second (ups).

Fails with 16 ups.

---

# Vertical Scaling: M3 XX-Large Instance

.fx: img-left

![M3 XX-Large Instance Graph](img/vertical_scaling_m3_xxlarge.png)

* 8 vCPUs
* 30 GB Memory
* SSD storage
* $400 per month
* Largest available M-prefixed instance.

Handles 16 new users per second (ups).

Fails with 20 ups.

---

# Vertical Scaling: C3 4XLarge Instance

.fx: img-left

![C3 4XLarge Instance Graph](img/vertical_scaling_c3_4xlarge.png)

* 16 vCPUs
* 30 GB Memory
* SSD storage
* $600 per month

Handles 20 new users per second (ups).

Fails with 25 ups.

---

# Load Balancing

Vertical scaling has its place, but horizontal scaling is generally preferable.

When horizontally scaling HTTP, this technique is referred to as __load
balancing__.

## Basic Idea

* Have many servers that can server clients
* Make these servers _appear_ as single endpoint to the outside world

The users' experiences are the same regardless of which server ultimately
handles the request.

---

# Think About It

> How can we enable many servers to serve clients?

Consider the following sequence of actions:

1. GET /products
2. POST /products
3. GET /products

> If these requests are handled by three different servers, will the third
> request show the new product?

---

# Stateless Servers

.fx: img-left

![Load Balanced Topology](img/load_balanced_topology.png)

In order for load balancing to work, the servers must be stateless.

Statelessness can be accomplished by keeping the persistence layer separate
from the application layer.

---

# Load Balancing (1): HTTP Redirects

.fx: img-left

![Load balancing via redirect](img/load_balancing_redirect.png)

Discussed in section 6.1 of the reading.

Implemented using multiple web servers with different domain names.

A request for www.domain.com will use HTTP 301 or 302 to redirect the request
to a pool of possible hosts.

---

# HTTP Redirect Example

    !http
    % nc www.domain.com 80
    GET / HTTP/1.1
    host: www.domain.com

    HTTP/1.1 301 Moved Permanently
    Date: Wed, 15 Oct 2014 21:08:22 GMT
    Server: Apache/2.2.22 (Ubuntu)
    Location: http://www2.domain.com/
    Content-Type: text/html; charset=iso-8859-1
    ...

---

# HTTP Redirects Trade-offs

## Strengths

* Simple
* Complete control over load balancing algorithm
* Location independent

## Weaknesses

* Not transparent to user
* High load on www
* May reduce local-network cache applicability

---

# Load Balancing (2): Round Robin DNS

.fx: img-left

![Load balancing via round-robin DNS](img/load_balancing_round_robin.png)

Discussed in section 4.1 of the reading.

When user's browser queries DNS for www.example.com, a list of IPs is
returned. The DNS server rotates the list order for each query (or alters
priorities).

User's browser chooses which IP to connect to (generally picks the first, or
highest priority).

---

# Round Robin DNS Example

    % host www.google.com
    www.google.com has address 74.125.224.48
    www.google.com has address 74.125.224.51
    www.google.com has address 74.125.224.52
    www.google.com has address 74.125.224.49
    www.google.com has address 74.125.224.50

    % host www.google.com
    www.google.com has address 74.125.224.49
    www.google.com has address 74.125.224.52
    www.google.com has address 74.125.224.51
    www.google.com has address 74.125.224.50
    www.google.com has address 74.125.224.48

---

# Round Robin DNS Trade-offs

## Strengths

* Simple
* Cheap

## Weaknesses

* Less control over balancing
* Modifying the list is inhibited by caching in the browser and proxies

---

# Load Balancing (3): TCP Load Balancing

.fx: img-left

![Load balancing via TCP](img/load_balancing_tcp.png)

Discussed in section 5 of the reading.

## General Idea

Rewrite TCP packets to send them to the selected server. This includes
addresses, sequence numbers, and checksums.


## Commercial Products (use hardware ASICs to do this fast)

* Cisco Content Services Switch
* Citrix Netscaler
* F5 Big IP

---

# TCP Load Balancing Example 1

__ client -> switch : 216.64.159.149 -> 208.50.157.136
IP D=208.50.157.136 S=216.64.159.149 LEN=60, ID=48397 2.94950 216.64.159.149 -> 208.50.157.136
TCP D=80 S=1421 Syn Seq=899863543 Len=0 Win=32120 …

__ switch -> client : 208.50.157.136 -> 216.64.159.149
IP D=216.64.159.149 S=208.50.157.136 LEN=48, ID=26291 2.95125 208.50.157.136 -> 216.64.159.149
TCP D=1421 S=80 Syn Ack=899863544 Seq=1908949446 Len=0 ...

__ client -> switch : 216.64.159.149 -> 208.50.157.136
IP D=208.50.157.136 S=216.64.159.149 LEN=40, ID=48400 2.98324 216.64.159.149 -> 208.50.157.136
TCP D=80 S=1421 Ack=1908949447 Seq=899863544 Len=0 ...

__ client -> switch : 216.64.159.149 -> 208.50.157.136
IP D=208.50.157.136 S=216.64.159.149 LEN=154, ID=48401 2.98395 216.64.159.149 -> 208.50.157.136
TCP D=80 S=1421 Ack=1908949447 Seq=899863544 Len=114 ... 2.98395 216.64.159.149 -> 208.50.157.136
HTTP GET /eb/images/ec_home_logo_tag.gif HTTP/1.0

---

# TCP Load Balancing Example 2

__ switch -> server : 216.64.159.149 -> 10.16.100.121
IP D=10.16.100.121 S=216.64.159.149 LEN=48, ID=26292 0.00000 216.64.159.149 -> 10.16.100.121
TCP D=80 S=1421 Syn Seq=899863543 Len=0 Win=32120 Options...

__ server -> switch : 10.16.100.121 -> 216.64.159.149
IP D=216.64.159.149 S=10.16.100.121 LEN=44, ID=22235 0.00001 10.16.100.121 -> 216.64.159.149
TCP D=1421 S=80 Syn Ack=899863544 Seq=2156657894 Len=0 ...

__ switch -> server : 216.64.159.149 -> 10.16.100.121
IP D=10.16.100.121 S=216.64.159.149 LEN=154, ID=48401 0.00131 216.64.159.149 -> 10.16.100.121
TCP D=80 S=1421 Ack=2156657895 Seq=899863544 Len=114 ... 0.00131 216.64.159.149 -> 10.16.100.121
HTTP GET /eb/images/ec_home_logo_tag.gif HTTP/1.0

---

# TCP Load Balancing Example 3

__ server -> switch : 10.16.100.121 -> 216.64.159.149
IP D=216.64.159.149 S=10.16.100.121 LEN=40, ID=22236 0.00134 10.16.100.121 -> 216.64.159.149
TCP D=1421 S=80 Ack=899863658 Seq=2156657895 Len=0 …

__ switch -> client : 208.50.157.136 -> 216.64.159.149
IP D=216.64.159.149 S=208.50.157.136 LEN=40, ID=22236 2.98619 208.50.157.136 -> 216.64.159.149
TCP D=1421 S=80 Ack=899863658 Seq=1908949447 Len=0 ...

__ server -> switch : 10.16.100.121 -> 216.64.159.149
IP D=216.64.159.149 S=10.16.100.121 LEN=1500, ID=22237 0.00298 10.16.100.121 -> 216.64.159.149
TCP D=1421 S=80 Ack=899863658 Seq=2156657895 Len=1460 ... 0.00298 10.16.100.121 -> 216.64.159.149
HTTP HTTP/1.1 200 OK

__ switch -> client : 208.50.157.136 -> 216.64.159.149
IP D=216.64.159.149 S=208.50.157.136 LEN=1500, ID=22237 2.98828 208.50.157.136 -> 216.64.159.149
TCP D=1421 S=80 Ack=899863658 Seq=1908949447 Len=1460 ... 2.98828 208.50.157.136 -> 216.64.159.149
HTTP HTTP/1.1 200 OK

---

# TCP Load Balancing Trade-offs

## Strengths

* More control over which requests go to which servers
* Works fine with HTTPs

## Weaknesses

* Constrains where the servers can be located (same network)
* Complicated

---

# Load Balancing (4): HTTP Proxy

.fx: img-left

![Load balancing via TCP](img/load_balancing_http_proxy.png)

Also known as "Layer 6 load balancing"

Terminate HTTP requests: act like a web server

Issue _back-end_ HTTP request to the desired application server.

Hardware products:

* Citrix Netscaler
* F5 Big-IP

Many HTTP servers have modules to do this as well (Apache, NGINX)

---

# HTTP Proxy Trade-offs

This is the most popular technique in use (#3 is also used).

## Strengths

* Cleaner implementation than packet rewriting

## Weaknesses

* Load balancer needs to do more work
* HTTPs is more complicated

---

# Think About It

Assume you are to design a load balancing HTTP proxy. You have insight into
every incoming request and response.

> How would you determine which server to forward a request to?

---

# Load Balancing Considerations

> How would you determine which server to forward a request to?

## Options

* Random
* Round robin
* Least number of connections
* Fastest response time
* Bandwidth per server
* URI-based mapping (e.g., `/images` to server1, `/admin` to server2)

Amazon's ELB (elastic load balancer) uses round robin with cookie-based
stickiness (send the same client to the same server).

---

# Load Balancing Challenges

When working with and/or designing a load balancing proxy there are some
challenges to consider.

* Detecting and reacting to server failures
* Session affinity and persistence
* Connection pooling

__Affinity__: Map a client to a server without application-level information
(e.g., IP address, request time)

__Persistence__: Use application-level
information to map a client to a server (e.g., cookies)

---

# Detecting Server Failures

> How do we know when a member of our application pool has died?

Observe traffic. Are requests being processed? Are they just taking a long
time?

Probe the server through various means:

* __ICMP ping__: tests the network and server kernel
* __TCP connection__: the process is running and accepting connections
* __HTTP HEAD__: the application is serving pages
* __SNMP__: Provides insight into server load (and more if configured)

---

# Session Affinity and Persistence

> Can we redirect users back to the same web server they used before?

Doing so can provide some caching improvements.

A few options:

* Affinity based on client IP address (concerns: client IPs change, and IPs are
shared)
* HTTP Cookie (works but requires proxy configuration)
* Session ID in URL (not a great solution)

---

# Connection Pooling

We're used to the idea that one client reuses a TCP connection for many HTTP
requests.

We can reuse this mechanism for distinct clients.

Saves on repeated TCP setup between the load balancer and application servers.

Reduces idle waiting on server for reads and writes.

---

# Software Load Balancers

* Apache
* NGINX
* HAProxy
* Varnish
* Pound
* Squid

---

# Amazon Elastic Load Balancer

Amazon provides load balancing as a service.

* $0.025 per load balancer hour
* $0.008 per GB of data processed
* Works with EC2 autoscaling groups
* Supports TLS termination
* Supports load balancing between Availability Zones within a Region

__Does not__: support load balancing between regions (e.g., between us-west-1
and us-west-2). Consider using route 54 DNS for region failover.

---

# Horizontal Scaling Test

In the vertical scaling tests, the database application ran on the same machine
as the web server application.

For these tests we are going to use a single machine for the database. This
will make it easy to scale up the number of application servers.

![Single Server Load Balanced Topology](img/load_balanced_topology_single.png)

---

# Horizontal Scaling: 1 M3 Large Instance

.fx: img-left

![Single M3 Large Instance Graph](img/horizontal_scaling_1.png)

* 2 vCPUs
* 7.5 GB Memory
* SSD storage
* DB is also M3 large
* $200 per month ($100 each)

Handles 10 new users per second (ups).

Fails with 16 ups.

Comparable to single M3 XLarge ($200/mo)

---

# Adding an App Server

Let's scale horizontally by adding a second application server instance.

![Dual Server Load Balanced Topology](img/load_balanced_topology_double.png)

---

# Horizontal Scaling: 2 M3 Large Instances

.fx: img-left

![Dual M3 Large Instance Graph](img/horizontal_scaling_2.png)

* 2 vCPUs
* 7.5 GB Memory
* SSD storage
* DB is also M3 large
* $300 per month ($100 each)

Handles 20 new users per second (ups).

Fails with 25 ups.

Comparable to single C3 4XLarge ($600/mo)

---

# More App Servers!

.fx: img-left

![5x Load Balanced Topology](img/load_balanced_topology_5x.png)

Let’s see how the system performs if we scale out to 5 app servers.

Total dollar cost will be comparable to the most expensive single instance we
tested.

---

# Horizontal Scaling: 5 M3 Large Instances

.fx: img-left

![Five M3 Large Instance Graph](img/horizontal_scaling_5.png)

* 2 vCPUs
* 7.5 GB Memory
* SSD storage
* DB is also M3 large
* $600 per month ($100 each)

Handles 35 new users per second (ups).

Handles 45 ups with an increase in response time.

Fails with 55 ups.

Single C3 4XLarge ($600/mo) failed at 25 ups!

---

# Horizontal Scaling FTW!

Vertical scaling handled only 20 new users per second at a cost of about $600
per month. There was no clear scaling path after that point.

Horizontal scaling handled 45 new users per second at a cost of about $600 per
month. The scaling path is clear. Add more servers for a linear increase in
cost.

_FTW_: For the Win

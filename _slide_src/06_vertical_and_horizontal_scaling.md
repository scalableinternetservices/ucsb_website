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

* __PRO__: Easy to add more servers (limited by datacenter space)
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

# Horizontal Scaling

---

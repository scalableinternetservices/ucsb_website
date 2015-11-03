# RDBMS Scaling and Service Oriented Architectures
.fx: title

__CS290B__

Dr. Bryce Boe

November 3, 2015

---

# Today's Agenda

* TODO
* RDBMS

---

# TODO

* Write Tsung xml file containing a single-complete session
* Use XML file to establish a baseline load test

---

# Motivation

You have your web application running on EC2. It is becoming increasingly
popular and performance is degrading.

> What do you do?

---

# Handling Concurrent Requests

You have deployed application servers that can serve many concurrent requests.

But as your site's popularity continues to grow that is not sufficient.

> What do you do?

# Vertical Scaling

You have increased your instance sizes and handled more load.

However, as the popularity continues to grow you are no longer able to continue
scaling vertically.

> What do you do?

---

# Horizontal Scaling

You have introduced a load balancer that distributes traffic across a pool of
application servers.

Nevertheless, as the traffic continues to increase, additional horizontal
scaling of the application servers does not solve the problem.

> What do you do?

---

# Caching

You have properly configured HTTP caching such that unnecessary requests never
happen.

You are also caching heavyweight database operations.

But it is still not enough to handle the increased load of your popular site.

> What do you do?

---

# SQL Structure and Query Optimization

You have reduced the number of queries your application servers makes to the
database.

You have used `EXPLAIN` to discover indexes to add, and to ensure your most
common SQL queries are as optimal as possible.

However, your database is still a bottleneck.

> What do you do?

---

# Database Vertical Scaling

> Is your database swapping (out of memory)?

Scale up the amount of memory.

> Is your database load too high?

Scale up the CPU.

> Are neither of those working?
> What do you do?

---

# Database Horizontal Scaling?

With application servers we are able to scale horizontally by adding additional
machines and introducing a load balancer to access them.

> Can we do the same with the database?

---

# Non-trivial DB Horizontal Scaing

 > Can we horizontally scale the database by adding more database servers and
 > accessing them through a load balancer?

Unfortunately, it's not that simple.

Horizontal scaling works great for _stateless_ services. However, the database
contains the state of our application, thus is not trivial to horizontally
scale.

---

# R(X), W(X), R(X)

TODO: Image of load balanced operations.

---

# Scaling Relational Databases

In a future lecture we will discuss scaling the data layer using non-relational
databases (NoSQL).

Today we will discuss in what ways we __can__ horiztonally scale a relational
database.

---

# Three Techniques

Each of the following techniques partitions RDBMS in a different way:

* Sharding
* Service Oriented Architectures (SOA)
* Separating Reads from Writes

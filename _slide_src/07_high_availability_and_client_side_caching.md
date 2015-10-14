# High Availability and Client-side Caching
.fx: title

__CS290B__

Dr. Bryce Boe

October 15, 2015

---

# Today's Agenda

* TODO
* Scaling Review
* Corrections
* High Availability
* Client-side Caching

---

# TODO

## Should be done

* Agile Web Development with Rails up through chapter 17
* As much progress on Sprint 1 commitment as possible

---

# Scaling Review

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

# Last Lecture Corrections

HTTP Reverse Proxies are Layer __7__ (not layer __6__)

The TCP session example demonstrates a TCP proxy version of load
balancing. While this approach works, it requires a TCP connection from the
client to the load balancer and another connection form the load balancer to
the server.

Of course the load balancer can maintain a pool of connections to
each application server minimizing the overhead of TCP connection
establishment.

The other version of TCP load balancing simply rewrites packets (both incoming
and outgoing). This process is similar to how NAT (network address translation)
works.

ELB's TCP-level load balancing does it via the TCP proxy method.

---

# High Availability Motivation

Modern web applications power some very important parts of our lives.

* Banking
* Medical
* Telephony

Having anytime access to these services (high availability) is increasingly
important.

---

# Expressing Availability

Companies offering services will often advertise some number of nines
availability:

* Three nines: 99.9% uptime, 525.6 minutes of downtime a year (43.8/mo)
* Four nines: 99.99% uptime, 52.6 minutes of downtime a year (4.38/mo)
    * Desired by many business applications
* Five nines: 99.999% uptime, 5.3 minutes of downtime a year (26.5s/mo)
    * Desired by communication companies

Downtime usually only includes unplanned outages. Scheduled outages, no matter
how frequent, are usually not incorporated in marketing material.

---

# Question

> What are possible causes of failures?

![Full network topology](img/full_stack.png)

---

# What if...

> What are possible causes of failures?

* a server process hangs?
* a server process dies?
* an application server fails?
* the load balancer fails?
* the switch fails?
* the router fails?
* the Internet fails?
* the database fails?
* the entire datacenter fails?

---

# Handling Application Server Failure

.fx: img-left

![Single application server](img/application_server.png)

We've already discussed the components of this sort of failure.

* Process-level isolation reduces hanging, or dead processes by having other
  processes to pick up the slack.
* A process in an infinite loop may add unnecessary load to the server, so it's
  important to have monitoring to detect such issues.
* Having a load-balanced configuration permits failing servers (high load or
dead) by having a pool of other servers to direct traffic to.

---

# How do we Handle Load Balancer Failure?

![Single load balancer](img/single_load_balancer.png)

---

# Redundant Load Balancers

.fx: img-left

![Redundant load balancers](img/redundant_load_balancers.png)

Buy two load balancers. One is the primary, and the other is the failover.

Load balancers communicate via a heartbeat to determine the health of each
other.

* _During a failover, what happens to established flows?_
* _During a failover, what happens to the IP address?_

---

# Load Balancer Failover

When the failure determines it needs to become the primary (detected via lack
of heartbeat), it issues a gratuitous ARP for the load balanced IP.

The gratuitous ARP (layer 2) will inform the switch that traffic should be
delivered to the port that leads to the former failover (now primary).

All new packets will transparently be delivered to the new primary load
balancer.

Established flows can be supported depending on how much information sharing
occurs between the load balancers.

---

# How do we Handle Switch Failure?

![Redundant load balancers](img/redundant_load_balancers.png)


---

# Redundant Switches

Buy two switches! Again with a primary and failover and a heartbeat.

During failover similar issues occur but layer 2 should be stateles so no/less
synchronization needed.

![Redundant switches](img/redundant_switches.png)

---

# How do we Handle Router Failure?

![Redundant switches](img/redundant_switches.png)

---

# Redundant Routers

Buy two!

Similar heartbeat and failover system, with slightly different problems.

![Redundant routers](img/redundant_routers.png)

---

# How do we Handle Internet Failure?

Buy two! Use separate internet service providers (ISPs).

![Redundant routers](img/redundant_routers.png)

---

# Routing with Two ISPs

> How do we handle routing when we have two ISPs?

## Outgoing Traffic (easy)

We control how we send outbound traffic so we have some options:

* Pick the cheapest or most reliable link
* Pick the _closer_ link

## Incoming Traffic (hard)

We cannot inform clients by which path to reach our IP.

However, we can give hints by using BGP to persuade networks to prefer one path
over another. (Path prepending, Community values)

---

# High Availability

![High Availability Topology](img/high_availability.png)

We will discuss database failover in another lecture.

---

# Redundancy Everywhere!

So we have redundant systems in place.

> Can anything go wrong?

---

# Disaster Strikes

![Hurricane Sandy from Satellite](img/hurricane_sandy_satellite.png)

---

# Hurricane Sandy via Ars Technica

![Hurrican Sandy Headline](img/hurricane_sandy_article.png)

---

# Availability Axiom (Pete Tenereillo)

Source: [http://www.tenereillo.com/GSLBPageOfShame.htm](http://www.tenereillo.com/GSLBPageOfShame.htm)

> The only way to achieve high-availability for browser based clients is to
> include the use of multiple A records.


An A record is an IP address associated with a DNS host.

## Result

* For performance we want to send the browser to one datacenter.
* For availability we want to send the browser multiple A records.

We end up having to make a choice between performance and availability.

---

# Multisite High Availability

![High Availability in Two Sites](img/dual_site_availability.png)


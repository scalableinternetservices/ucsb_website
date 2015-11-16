# HTTP 2.0 and QUIC
.fx: title

__CS290B__

Dr. Bryce Boe

November 17, 2015

---

# Today's Agenda

* HTTP Optimization Hacks
* HTTP 2.0
* QUIC

---

# Connections per Page

![Connections per page](img/connections_per_page.png)

Many requests are required for today's web pages:

* CSS
* Javascript
* Images

Source: [http://httparchive.org](http://httparchive.org)

---

# TCP Phases

![TCP Phases](img/tcp_congestion.png)

Establishing many TCP connections to serve these resources is very slow.

Source: High Performance Browser Networking

---

# TCP Round Trips

![Number of TCP Segments v. Round Trips](img/tcp_segments_and_round_trips.png)

TCP was designed for long-lived flows. HTTP is short and bursty.

---

# HTTP Keepalive

.fx: img-left

![Head of Line Blocking](img/tcp_head_of_line_blocking.png)

HTTP Keepalive was introduced to help reuse TCP connections for HTTP, but there
are issues.

While we can resuse a TCP socket for multiple HTTP requests, one heavyweight
request can starve all others.

This is called __Head-of-line blocking__.

---

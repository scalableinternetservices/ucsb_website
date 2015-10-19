# Server-side Caching and Deploying on AWS
.fx: title

__CS290B__

Dr. Bryce Boe

October 20, 2015

---

# Today's Agenda

* High Availability Review
* Client-Side Caching Review
* Server-side Caching
* Deploying on Amazon Web Services (AWS)

---

# High Availability Review

![High Availability in Two Sites](img/dual_site_availability.png)

---

# Client-side Caching Review

![Defining optimal Cache-Control policy](img/http-cache-decision-tree.png)

Source: [https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching)

---

# Client-side Caching in Rails

* Use `stale?` if you want to conditionally execute a section of code only
  if the client doesn't have a cached version.

* Use `fresh_when` if you only want to use/set the cache headers.

---

# Goals for Today

## After today you should understand...

* why server-side caching exists
* what options you have when using server-side caching
* how to use server-side caching in your projects
* how to deploy on AWS using CloudFormation

---

# Caching HTTP Responses: Motivation

A single web server process repeatedly responds to HTTP requests from a variety
of clients.

Responding to each request requires computation and/or I/O to be
performed, both of which can be expensive.

In practice, there is a significant amount of similarity between HTTP
responses.

In the client-side caching lecture we looked at optimizing scenarios where
requests for the same resource would result in an identical response.

In this lecture we will look at optimizing scenarios where repeated responses
are not identical, but similar.

---

# Caching HTTP Responses

> With respect to HTTP responses for a single web service, which parts of a
> response are similar to responses for other resources?

---

# Caching HTTP Responses

> With respect to HTTP responses for a single web service, which parts of a
> response are similar to responses for other resources?

* View fragments
* Rarely modified ORM objects
* Expensive to compute data

---

# View Fragments

View fragments are items that are similar across pages such as the header,
footer, sidebar, or even an item listing that may appear in multiple locations
(product listings, search results, product suggestions).

Sidebar Fragment (shown on all cs290.com pages)

    !html
    <div class="col-md-3 hidden-xs">
      <div class="sidebar well">
        Scalable Internet Services, CS290B, Fall 2015
      </div>

      <div class="sidebar well">
        <h1 id="course-information">Course Information</h1>
        <h2 id="instructor">Instructor</h2>
        <p><a href="http://cs.ucsb.edu/~bboe">Dr. Bryce Boe</a>

        <h2 id="lecture">Lecture</h2>
        <p>Tuesday and Thursday<br />
           3:00pm – 4:50pm</p>

        ...

      </div>
    </div>

---

# Rarely Modified ORM Objects

* User permissions
* Configuration options
* Product details (on a shopping site)
* In general, any database-backed data that seldom changes

---

# Expensive to Compute Data

Expensive to compute data is exactly what the name suggests. Expensive may mean
it takes a significant amount of time to compute, or maybe it is best suited
for a background worker due to hardware constraints on the application servers.

## Examples

* Total account balance on Mint
* Monthly account summary on Google
* The complete diff between two commits on GitHub
* The list of suggested contacts on LinkedIn

---

# Semi-Expensive Operations

View fragments are produced by extensive string manipulation. In ruby, many
string manipulations with portions loaded from disk can result in a significant
amount of time.

Every query to the database utilizes its resources. Optimizing for similar
queries can minimize the chance of a database bottleneck.

> Assuming we want to keep previously computed results around between requests,
> how can we do it?

> Where can we store the cached results?

---

# Storing Cached Results

Option 1: In memory on the application server

Option 2: On the filesystem

Option 3: In memory on another machine

Now, let's look into each of these options. But first a look at latency.

---

# Latency Numbers (ns and μs)

![Latency Numbers Every Programmer Should Know](img/latency_1_2015.png)

Source: http://www.eecs.berkeley.edu/~rcs/research/interactive_latency.html

---

# Latency Numbers (μs and ms)

![Latency Numbers Every Programmer Should Know](img/latency_2_2015.png)

Source: http://www.eecs.berkeley.edu/~rcs/research/interactive_latency.html

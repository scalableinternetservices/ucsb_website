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

---

# Latency Numbers for Caching

* Storing in memory and reading later is fast
    * Random reads from memory is < 0.1μs
    * Reading 1MB is 9μs
* Storing on disk is slow without SSD (solid state drive):
    * Disk seek is 4000μs
    * Subsequent sequential read of 1MB is 2000μs
* Storing on disk with SSD is much more reasonable
    * Random read is 16μs
    * Sequential read of 1MB is 156μs
* Storing on another machine is reasonable
    * Round trip within datacenter is 500μs

---

# Latency Numbers Summary

## Summary

* In memory: tens of μs
* On SSD: hundreds of μs
* On magnetic disk: thousands of μs
* On remote machine: add hundreds of μs

## Conclusions

* Always use SSD over magnetic storage
* Memory > SDD > Remote

> Are these conclusions always true?

---

# Caching Locations

> What effect on the cache hit rate does each of these designs have?

* In memory: cache per process
* On SSD: Cache per machine
* On remote machine: Cache per application server pool (cluster)

---

# Caching Location Trade-offs

* In memory
    * highest performance
    * lowest hit rate
* On SSD
    * lower performance
    * higher hit rate
* On remove machine
    * lowest performance
    * highest hit rate

There is no silver bullet.

---

# Caching Trade-offs

> How will each of the following affect system performance:

* Number of processes per machine
* Concurrency model of application server
* Number of machines per cluster

---

# Memcached

__memcached__ is a commonly used remote cache server. It...

* keeps a cache in memory
* provides a simple TCP protocol to return responses to lookup requests
* is a distributed key-value store
    * keys can be up to 250 bytes
    * values can be up to 1MB
    * scales horizontally
* uses a simple LRU (least recently used) to make space for new items when full
* performs all operations in constant time

---

# Server-side Caching in Rails

Rails provides excellent support for server-side caching.

The three primary interfaces to caching in rails are:

* HTTP caching
* Fragment caching
* Low level caching

We already covered HTTP caching. Today we'll discuss the latter two.

---

# Enabling Caching in Rails

By default, caching is disabled in development and test modes, and enabled only
in production mode.

If you want to enable caching in development mode you must make the following
change to your Rails environment:

    !ruby
    config.action_controller.perform_caching = true

Rails can be configured to store cached data in a few different places:

* In memory
* On a _local_ file system
* In a remote in-memory store

---

# Rails Cache Stores

## ActiveSupport::Cache::MemoryStore

* Cached data is storred in memory, in the same address space as the ruby
  process.
* Defaults to 32MB, configurable

## ActiveSupport::Cache::FileStore

* Cached data is stored on the _local_ file system.
* Can configure the location of the storage in the Rails environment:

        !ruby
        config.cache_store = :file_store, '/path/to/cache/'

## ActiveSupport::Cache::MemcacheStore

* Cached data is stored in memory on another machine (could also be local).
* Can configure the location of the server in the Rails environment:

        !ruby
        config.cache_store = :mem_cache_store, 'cache-1.example.com'

---

# Rails: Fragment Caching

Fragment caching caches a portion of a rendered view for reuse on future
requeusts.

Let's look at fragment caching in the context of the demo app.

---

# Fragment Caching Submission Partials

.fx: img-left

![Submissions Index View](img/demo_submissions_index.png)

We can cache each submission listing.

With that done, then regardless of any other changes on the page, we can
rerender the submission view for all submissions that haven't been updated.

---

# Submission Listing (without cache)

    !erb
    <% @submissions.each do |submission| %>
      <tr>
        <td><%= link_to(submission.title, submission.url) %></td>
        <td><%= submission.url %></td>
        <td><%= submission.community.name %></td>
        <td>
          <%= link_to("#{submission.comments.size} comments",
                      submission, class: 'btn btn-primary btn-xs') %>
        </td>
      </tr>
    <% end %>

---

# Submission Listing (with cache)

    !erb
    <% @submissions.each do |submission| %>

      <% cache(cache_key_for_submission(submission)) do %>

      <tr>
        <td><%= link_to(submission.title, submission.url) %></td>
        <td><%= submission.url %></td>
        <td><%= submission.community.name %></td>
        <td>
          <%= link_to("#{submission.comments.size} comments",
                      submission, class: 'btn btn-primary btn-xs') %>
        </td>
      </tr>

      <% end %>

    <% end %>

---

# Chosing a Cache Key

> How should we choose a cache key?

    !ruby
    module SubmissionHelper
      def cache_key_for_submission(submission)
        "submission/#{submission.id}"
      end
    end

> What are the weaknesses with the above approach?

---

> How should we choose a cache key?

    !ruby
    module SubmissionHelper
      def cache_key_for_submission(submission)
        "submission/#{submission.id}"
      end
    end

> What are the weaknesses with the above approach?

* Invalidation will need to be explicit as the submission ID will rarely, if
  never, be updated for an object.
* Explicitly invalidating cache items can easily make a mess of the code.

---

# Chosing a Better Cache Key

    !ruby
    module SubmissionHelper
      def cache_key_for_submission(sub)
        "submission/#{sub.id}/#{sub.updated_at}/#{sub.comments.count}"
      end
    end

With the above, a submission's fragment cache is invalidated anytime the
submission is updated (`updated_at` is always updated), or when the number of
comments assocaited with the submission changes.

_Note_: An Active Record model can be used directly as the key. It calls an
overwritable method `cache_key` on the model. By default that method returns a
key that "includes the model name, the id and finally the updated_at
timestamp".

Reference:
[http://guides.rubyonrails.org/caching_with_rails.html#fragment-caching](http://guides.rubyonrails.org/caching_with_rails.html#fragment-caching)

---

# More Fragment Caching

.fx: img-left

![Submissions Index View](img/demo_submissions_index.png)

Now we are caching a fragment for each submission.

> What else can we cache?

---

# More Fragment Caching

.fx: img-left

![Submissions Index View](img/demo_submissions_index.png)

Now we are caching a fragment for each submission.

> What else can we cache?

We can cache the entire submission listing!

---

# Community Listing (without cache)

    !erb
    <h3>Submissions</h3>
    <table class="table">
      <thead>
        <tr>
          <th>Title</th>
          <th>Url</th>
          <th>Community</th>
          <th colspan="3"></th>
        </tr>
      </thead>

      <tbody>
        <% @submissions.each do |submission| %>
          <% cache(...) do %> ... <% end %>
        <% end %>
      </tbody>
    </table>

    ...

---

# Community Listing (with cache)

    !erb
    <% cache(cache_key_for_submission_table) do %>

    <h3>Submissions</h3>
    <table class="table">
      <thead>
        <tr>...</tr>
      </thead>

      <tbody>
        <% @submissions.each do |submission| %>
          <% cache(...) do %> ... <% end %>
        <% end %>
      </tbody>
    </table>

    ...

    <% end %>
---

# cache_key_for_submission_table

    !ruby
    module SubmissionHelper
      def cache_key_for_submission(sub)
        "submission/#{sub.id}/#{sub.updated_at}/#{sub.comments.count}"
      end

      def cache_key_for_submission_table
        ("submission_table/#{Submission.maximum(:updated_at)}/"
         + Comment.maximum(:updated_at).to_s)
      end
    end

This technique of nesting cache fragments is known as __Russian Doll Caching__.

---

# Low-level Rails Caching

You can use the same built-in mechanisms to manually cache anything:

    !ruby
    class Product < ActiveRecord::Base
      def competing_price
        Rails.cache.fetch("#{cache_key}/competing_price",
                          expires_in: 12.hours) do
          Competitor::API.find_price(id)
        end
      end
    end

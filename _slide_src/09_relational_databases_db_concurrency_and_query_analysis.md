# Relational Databases: Concurrency Control and Query Analysis
.fx: title

__CS290B__

Dr. Bryce Boe

October 22, 2015

---

# Today's Agenda

* TODO
* Server-side Caching in Rails Review
* Motivation
* A Stable Data Layer
* Database Concurrency Control
* Query Analysis

---

# TODO

## By end of lab

* As a team, launch your application on AWS
* Individually, confirm that you are able to SSH into your instance
* Shutdown your AWS stack(s)

---

# Server-side Caching in Rails Review

---

# Rails Russian Doll Caching

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

---

# Motivation

After today you should...

* understand the importance of relational databases in architecting scalable
  Internet systems
* understand how to design with concurrency in mind
* have a basic idea regarding how to speed up your data layer
    * where to start
    * Rails-specific techniques
    * be able to identity the source of slowness in a SQL query

---

# Stateful Requests

.fx: img-left

![Database connectivity](img/app_server_to_database.png)

We have many stateless application servers responding to requests.

Clients can be served by any application servers.

Client requests regularly include data updates.

---

# Application Server _Needs_

.fx: img-left

![Database connectivity](img/app_server_to_database.png)

* Data needs to be shared between requests and servers

* Access to data shouldn't be slow

* High availability of shared data

* Utilizing the data layer should be intuitive:

        !ruby
        if david.balance > 100
          david.withdrawal(100)
          mary.deposit(100)
        end

---

# Data Layer Options

.fx: img-left

![Database connectivity](img/app_server_to_database.png)

There are quite a few existing solutions for a _stable_ data layer.

## Relational (SQL)

* MySQL (MariaDB, Percona)
* Postgresql
* Oracle
* MS SQL

## Non-relational (NoSQL)

* Cassandra
* MongoDB
* Redis

---

# SQL v. NoSQL

.fx: img-left

![Database connectivity](img/app_server_to_database.png)

## Relational Databases...

* are a general-purpose persistence layer
* offer more features
* have a limited ability to scale horizontally

## Non-relational Databases...

* often are more specialized
* require more from the application layer
* are better at scaling horizontally

If your needs fit within a RDBMS's (relational database management system)
ability to scale, they tend to be best. If your scaling needs exceed RDBMS
capabilities, go non-relational.

---

# Database Outline

.fx: img-left

![Database connectivity](img/app_server_to_database.png)

## Today we will discuss:

* Relational databases
* Concurrency control
* SQL query analysis

## Later we will discuss:

* Scaling options for relational databases:
    * Sharding
    * Service Oriented Architectures (SOA)
    * Distinguishing reads from writes
* A survey of NoSQL options

---

# Database Transactions

Transactions are a database concept that allows a system to guarantee certain
semantic properties.

Transactions provide control over concurrency.

Having rigorously defined guarantees means we can build correct systems using
these databases.

---

# Database Transaction History

## Mid 1970's, IBM System R's Research Storage System (RSS)

* First system to implement SQL
* Introduced formal notions of transactions and serializability

Jim Gray (1998 Turing Award Winner) had a significant role in the project for
the introduction of transactions.

---

# Database ACID Properties

## Atomicity

* Complete everything, or do nothing
* No partial application of a transaction

## Consistency

* The database should be consistent both at the beginning and end of a
  transaction
* Consistency is defined by the integrity constraints (e.g., foreign keys, `NOT
  NULL`, etc.)

## Isolation

* A transaction should not see the effects of other uncommitted transactions

## Durability

* Once committed, the transaction's effects should not disappear

---

# Overlapping Concerns

__Atomicity__ and __Durability__ are related and are generally provided by
_journalling_.

__Consistency__ and __Isolation__ are provided by concurrency control (usually
implemented via locking).

---

# Definition: Schedule

A __schedule__ is an abstract model used to describe the execution of
transactions that run in a database.

.fx: table-center

| T1     | T2     | T3     |
|:------:|:------:|:------:|
| R(X)   |        |        |
| W(X)   |        |        |
| Commit |        |        |
|        | R(Y)   |        |
|        | W(Y)   |        |
|        | Commit |        |
|        |        | R(Z)   |
|        |        | W(Z)   |
|        |        | Commit |

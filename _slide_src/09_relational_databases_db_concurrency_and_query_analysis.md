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

.fx: table-center

A __schedule__ is an abstract model used to describe the execution of
transactions that run in a database.


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

---

# Conflicting Actions

Two actions are said to be in conflict if:

* the actions belong to different transactions
* at least one of the actions is a write operation
* the actions access the same object (read or write)

## Conflicting Actions

| T1     | T2     | T3     |
|:------:|:------:|:------:|
| R(X)   |        |        |
|        | W(X)   |        |
|        |        | W(X)   |

---

# Non-Conflicting Examples

.fx: center

## All reads

| T1     | T2     | T3     |
|:------:|:------:|:------:|
| R(X)   |        |        |
|        | R(X)   |        |
|        |        | R(X)   |

## Write to different object

| T1     | T2     | T3     |
|:------:|:------:|:------:|
| R(X)   |        |        |
|        | W(Y)   |        |
|        |        | R(X)   |

---

# Question

> Can we blindly execute transaction in parallel?

---

# Answer

> Can we blindly execute transaction in parallel?

__No__

* Dirty Read Problem
* Incorrect Summary Problem

---

# Dirty Read Problem

.fx: table-center

A transaction (T2) reads a value written by another transaction (T1) that is
later _aborted_ (its actions are rolledback).

The result of the T2 transaction will put the database in an incorrect state.

| T1     | T2     |
|:------:|:------:|
| W(X)   |        |
|        | R(X)   |
| Abort  |        |
|        | W(Y)   |
|        | Commit |

---

# Incorrect Summary Problem

.fx: table-center

A transaction (T1) computes a summary over the values of all the instances of a
repeated data-item. While that occurs, another transaction (T2) updates some
instances of data-item.

The resulting summary will not reflect a correct result for any deterministic
order of the transactions (T1 then T2, or T2 then T1).

| T1     | T2     |
|:------:|:------:|
| R(X*)  |        |
| R(X*)  | W(X^n) |
| R(X*)  | Commit |
| R(X*)  |        |
| W(Y)   |        |
| Commit |        |

---

# Schedule Types

## A schedule is _serial_ if

* the transctions are executed non-interleaved

## Two schedules are _conflict equivalent_ if

* they involve the same actions of the same transactions
* every pair of conflicting actions are ordered in the same way

## A schedule is _conflict serializable_ if

* the schedule is __conflict equivalent__ to a __serial__ schedule

## A schedule is _recoverable_ if

* transactions commit only after all transactions whose changes they read,
  commit

---

# Not Conflict Serializable

.fx: table-left

| T1     | T2     |
|:------:|:------:|
| R(A)   |        |
| W(A)   |        |
|        | R(A)   |
|        | W(A)   |
|        | R(B)   |
|        | W(B)   |
| R(B)   |        |
| W(B)   |        |

When transactions are serialized, it is not conflict equivalent to either of:

| T1     | T2     |
|:------:|:------:|
| R(A)   |        |
| W(A)   |        |
| R(B)   |        |
| W(B)   |        |
|        | R(A)   |
|        | W(A)   |
|        | R(B)   |
|        | W(B)   |

| T1     | T2     |
|:------:|:------:|
|        | R(A)   |
|        | W(A)   |
|        | R(B)   |
|        | W(B)   |
| R(A)   |        |
| W(A)   |        |
| R(B)   |        |
| W(B)   |        |

---

# Why Serializable?

.fx: img-left

![Database connectivity](img/app_server_to_database.png)

> Why is it important that we have a serializable schedule?

> Why not simply execute serially?

---

# Serial Schedule

Having a serial schedule is important for consistent results. For example it is
good when you are keeping track of your bank balance in the database.

A serial execution of transactions is safe but _slow_.

Most general purpose relational databases default to employing
conflict-serializable and recoverable schedules.

> How do these RDBMS employ conflict-serializable and recoverable schedules?

---

# Database Locks

In order to implement a database whose schedules are both conflict serializable
and recoverable locks are used.

* A lock is a system object associated with a shared resource such as a data
  item, a row, or a page in memory.

* A database lock may need to be acquired by a transaction before accessing the
  object.

* Locks prevent undesired, incorrect, or inconsistent operations on shared
resources by concurrent transactions.

---

# Types of Database Locks

## Write-lock

* Blocks writes and reads
* Also called __exclusive lock__

## Read-lock

* Blocks writes
* Also called __shared lock__ (other reads can happen concurrently)

---

# Two-Phase Locking

Two-phase locking (2PL) is a concurrency control method that guarantees
serializability.

The two phases are:

* Acquire Locks
* Release Locks

## Two-phase locking Protocol

* Each transaction must obtain a _shared_ lock on an object before reading.
* Each transaction must obtain an _exclusive_ lock on an object before writing.
* If a transaction holds an exclusive lock on an object, no other transaction
  can obtaany lock on that object.
* A transaction cannot request additional locks once it releases any locks.

---

# Two-Phase Locking: Potential Issue

.fx: table-center

During the second phase locks can be released as soon as they are no longer
needed. This permits other transactions to obtain those locks.

| T1        | T2     |
|:---------:|:------:|
| R(A)      |        |
| W(A)      |        |
| unlock(A) |        |
|           | R(A)   |
| ...       | ...    |
| abort     |        |

> What happens to T2 when T1 aborts the transaction?

---

# Strong Strict Two-Phase Locking

2PL can result in cascading aborts.

SS2PL allows only conflict serializable schedules.

# Strong Strict Two-Phase Locking Protocol

* Each transaction must obtain a _shared_ lock on an object before reading.
* Each transaction must obtain an _exclusive_ lock on an object before writing.
* If a transaction holds an exclusive lock on an object, no other transaction
  can obtaany lock on that object.
* All locks held by a transaction are released when the transaction completes.

This approach avoids the problem with cascading aborts.

> What is the downside to SS2PL?

---

# Concurrency Control in Rails

.fx: img-left

![Database connectivity](img/app_server_to_database.png)

We have many application servers running our application.

We are using a relational database to ensure that each requests observes a
consistent view of the database.

> What it required in rails to obtain this consistency?

---

# Concurrency Control in Rails

Rails uses two types of concurrency control:

## Optimistic Locking

Assume that database modifications are going to succeed. Throw an exception
when they do not.

## Pessimistic Locking

Ensure that databases modifications will succeed by explicitly avoiding
conflict.

---

# Optimistic Locking in Rails

Any ActiveRecord model will automatically utilize optimistic locking if an
integer `lock_version` field is added to the object's table.

Whenever an such an ActiveRecord object is read from the database, that object
contains its associated `lock_version`.

When an update for the object occurs, Rails compares the object's
`lock_version` to the most recent one in the database.

If they differ a `StaleObjectException` is thrown.

Otherwise, the data is written to the database, and the `lock_version` value is
incremented.

This optimistic locking is an application-level construct. The database does
nothing more than storing the `lock_version` values.

---

# Optimistic Locking Example

    !ruby
    c1 = Child.find(1)
    c1.gender = "male"

    c2 = Child.find(1)
    c2.gender = "female"

    c1.save!  # Succeeds (It's a boy!)
    c2.save!  # throws StaleObjectException

## Strengths

* Predictable performance
* Lightweight

## Weaknesses

* Have to write error handling code
* (or) errors will propogate to your users

---

# Pessimistic Locking in Rails

Easily done by calling `lock` along with ActiveRecord `find`.

Whenever an ActiveRecord object is read from the database with that option an
exclusive lock is acquired for the object.

While this lock is held, the database prevents others from obtaining the lock,
reading from, and writing to the object. The others are blocked until the
object is unlocked.

Implemented using the `SELECT FOR UPDATE` SQL.

---

# Pessimistic Locking Example

Request 1

    !ruby
    transaction do
      c1 = Child.find(1).lock(true)
      c1.name = 'Daniel'
      c1.save!  # works fine
    end

Request 2

    !ruby
    transaction do
      c2 = Child.find(1).lock(true)
      c2.name = 'Evelyn'
      c2.save!  # works fine
    end

This approach works great, yet it is not commonly used.

> What could go wrong?

---

# Pessimistic Locking Issue 1

> What could go wrong? (blocking)

Request 1

    !ruby
    transaction do
      c1 = Child.find(1).lock(true)
      c1.name = 'Daniel'
      my_long_procedure
      c1.save!
    end

Request 2

    !ruby
    transaction do
      c2 = Child.find(1).lock(true)
      c2.name = 'Evelyn'
      c2.save!
    end

---

# Pessimistic Locking: Deadlock

Request 1

    !ruby
    transaction do
      fam = Family.find(3).lock(true)
      c1 = Child.find(1).lock(true)
      c1.name = 'Daniel'
      c1.save!
      fam.count += 1
      fam.save!
    end

Request 2

    !ruby
    transaction do
      c2 = Child.find(1).lock(true)
      c2.name = 'Evelyn'
      c2.save!
      fam = Family.find(3).lock(true)
      fam.count += 1
      fam.save!
    end

---

# Pessimistic Locking: Summary

## Strengths

* Failed transactions are incredibly rare or nonexistent

## Weaknesses

* Have to worry about deadlocks and avoiding them
* Performance is less predictable

---

# Challenge 1

> Which form of locking would you choose?

    !ruby
    transaction do
      determine_auction_winner()
      send_email_to_winner()
      save_auction_outcome()
    end

---

# Challenge 2

> Which form of locking would you choose?

    !ruby
    transaction do
      record_facebook_like()
      update_global_counter_of_all_likes_ever()
    end

---

# Query Analysis

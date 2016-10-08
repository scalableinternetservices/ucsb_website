# TDD, CI, Pairing, and Web Servers
.fx: title

__CS291A__

Dr. Bryce Boe

October 4, 2016

---

# Today's Agenda

* TODO
* Agile Review
* Test Driven Development
* Continuous Integration
* Github Workflow
* Pair Programming
* Web Servers

---

# TO-DO

## Should be done:

* Chapters 1, 2, 9-11 in
  [HPBN](https://hpbn.co/primer-on-latency-and-bandwidth/) / Chapter 1 in the
  [Ruby on Rails Tutorial](https://www.railstutorial.org/book/beginning)

## Before Tomorrow's Lab:

* Complete Chapters 2 through 6 in the
  [Ruby on Rails Tutorial](https://www.railstutorial.org/book/toy_app)
* Learn [git](http://rogerdudler.github.io/git-guide/)
* Your team's github should have a single-controller app and a README with
  project description, and team member photos.

---

# Agile Review

> ## Sprint 2: Starts October 12

> * Conduct a __retrospective__ on how the last sprint went and how your group
>   can improve.
> * Decide on a sprint commitment.
> * Implement stories from the current sprint.

---

# Test Driven Development

Assume we have a large group of software engineers working on the same project.

Every day, each engineer makes many changes to the project.

Human error is common and information is not global.

Errors will happen.

> How do we discover when errors occur?

---

# Discovering Errors

* Humans can be used to check for defects, but this is expensive

* Type systems and compilers work well to statically check for defects, but can
  only discover certain classes of errors.
    * Formal verification tools exist, but are not widely used in industry.

* Automated testing

---

# Automated testing...

* ... is writing testing code to execute your production code and make
  assertions about how it should behave

* ... can be measured by code coverage tools that determine which code paths
  are executed by your tests

* ... allows you to build large and complex systems with very permissive
  languages

    * For a dynamically typed language like Ruby, automated testing can make up
      for the lack of static checks normally done by a compiler

---

# Automated Testing: How?

__If automated testing is important and we want significant code coverage (not
necessarily 100%), how do we get there?__

* Don't write any production code, until there is test code that tests the
  desired functionality.
* Write the minimal amount of production code to make the test(s) pass.

## Steps

1. Write the test and observe a failure (__red__)
2. Write the production code and observe a pass (__green__)
3. Clean up your design of both the code and tests (__refactor__)

---

# TDD Example: FizzBuzz

* If the argument is divisible by three, return "Fizz"
* If the argument is divisible by five, return "Buzz"
* If the argument is divisible by both return "FizzBuzz"
* Otherwise return the argument

---

# Test Fizz (red)

## Test

    !ruby
    def test_divisible_by_3
      assert_equal 'Fizz', fizzbuzz(3)
    end

## Program

    !ruby
    def fizzbuzz(n)
      # test_divisible_by_3 fails
    end

---

# Test Fizz (green)

## Test

    !ruby
    def test_divisible_by_3
      assert_equal 'Fizz', fizzbuzz(3)
    end

## Program

    !ruby
    def fizzbuzz(n)
      'Fizz'
      # test_divisible_by_3 passes
    end

---

# Test Buzz (red)

## Test

    !ruby
    def test_divisible_by_5
      assert_equal 'Buzz', fizzbuzz(5)
    end

## Program

    !ruby
    def fizzbuzz(n)
      'Fizz'
      # test_divisible_by_3 passes
      # test_divisible_by_5 fails
    end

---

# Test Buzz (green)

## Test

    !ruby
    def test_divisible_by_5
      assert_equal 'Buzz', fizzbuzz(5)
    end

## Program

    !ruby
    def fizzbuzz(n)
      if n % 3 == 0
        'Fizz'
      else
        'Buzz'
      end
      # test_divisible_by_3 passes
      # test_divisible_by_5 passes
    end

---

# Test FizzBuzz (red)

## Test

    !ruby
    def test_divisible_by_both
      assert_equal 'FizzBuzz', fizzbuzz(15)
    end

## Program

    !ruby
    def fizzbuzz(n)
      if n % 3 == 0
        'Fizz'
      else
        'Buzz'
      end
      # test_divisible_by_3 passes
      # test_divisible_by_5 passes
      # test_divisible_by_both fails
    end

---

# Test FizzBuzz (green)

## Test

    !ruby
    def test_divisible_by_both
      assert_equal 'FizzBuzz', fizzbuzz(15)
    end

## Program

    !ruby
    def fizzbuzz(n)
      if n % 3 == 0
        if n % 5 == 0
          'FizzBuzz'
        else
          'Fizz'
        end
      else
        'Buzz'
      end
      # test_divisible_by_3 passes
      # test_divisible_by_5 passes
      # test_divisible_by_both passes
    end

---

# Test Other (red)

## Test

    !ruby
    def test_divisible_by_neither
      assert_equal 17, fizzbuzz(17)
    end

## Program

    !ruby
    def fizzbuzz(n)
      if n % 3 == 0
        if n % 5 == 0
          'FizzBuzz'
        else
          'Fizz'
        end
      else
        'Buzz'
      end
      # test_divisible_by_3 passes
      # test_divisible_by_5 passes
      # test_divisible_by_both passes
      # test_divisible_by_neither fails
    end

---

# Test Other (green)

## Program

    !ruby
    def fizzbuzz(n)
      if n % 3 == 0
        if n % 5 == 0
          'FizzBuzz'
        else
          'Fizz'
        end
      elsif n % 5 == 0
        'Buzz'
      else
        n
      end
      # test_divisible_by_3 passes
      # test_divisible_by_5 passes
      # test_divisible_by_both passes
      # test_divisible_by_neither passes
    end

---

# FizzBuzz Refactor

    !ruby
    def fizzbuzz(n)
      if n % 15 == 0
        'FizzBuzz'
      elsif n % 3 == 0
        'Fizz'
      elsif n % 5 == 0
        'Buzz'
      else
        n
      end
      # test_divisible_by_3 passes
      # test_divisible_by_5 passes
      # test_divisible_by_both passes
      # test_divisible_by_neither passes
    end

---

# Types of Tests

The previous FizzBuzz example demonstrated __unit__ tests. Other types of tests
are:

* Functional
* Integration
* System
* Acceptance

Whenever you discover a bug, the first thing you _should_ do is write a test
that demonstrates the failure caused by the bug. Then fix the code and observe
it passing. Building this set of tests helps prevent the introduction of a
_regression_.

---

# TDD Encouragement

When working on your projects I strongly recommend that you begin by trying out
test driven development.

High test coverage can help you avoid getting stuck on bugs, which is even more
important as more people are working on the same code.

Your grade does not depend on your code coverage, however, significant code
coverage will help to ensure a bug is not introduced prior to your team's
presentation (that would impact your grade).

---

# Integration

Taking independently developed changes and reconciling their conflicts.

Integration can be very difficult and painful.

> Should we perform integration as rarely as possible or as frequently as
> possible?

---

# Martin Fowler

.fx: img-left

Chief Scientist, ThoughtWorks

![Martin Fowler](img/martin_fowler.jpg)

_"The effort of integration is exponentially proportional to the amount of
time between integrations."_

---

# Reconcile Early and Often

If we never let our changes diverge too much from the rest of the group,
reconciling our changes will never be too hard.

__Conclusion__: commit early and often, and merge others' changes early and
often

> How do we ensure we have successfully reconciled?

---

# Continuous Integration

__Automated Tests!__

Utilize a __Continuous Integration__ server (CI) that will monitor changes to
your source code.

Whenever anyone checks in new code, run all the tests.

* The sooner you find and fix integration problems, the better.
* This also prevents defects unrelated to integration.

The CI server can also test code quality and security, among other things.

---

# CI via TeamCity

![APM Bundle Trunk Team City CI](img/apm_bundle_ci.png)

---

# CI via Travis CI

![Rails Travis CI](img/rails_ci.png)

---

# Travis CI

You will configure your projects to use Travis CI:
[https://travis-ci.org/](https://travis-ci.org/)

Travis CI is free for open-source projects.

If you are doing TDD and creating automated tests, Travis CI will provide you
with immediate feedback on your changes through GitHub:

![Github Pull Request "All is well"](img/github_pr_all_is_well.png)

---

# Other Related Tools

## Coveralls

Web service that provides view into code coverage that occurs during the
testing phase. Integrates with github and Travis ci and can be configured to
_fail_ pull requests that decrease code coverage.

[https://coveralls.io/](https://coveralls.io/)

Free for open source projects.

## Rubocop

A static analysis tool for ruby that suggests source code improvements
encompassing code style, unused variables, visually ambiguous statements, and
more.

[https://github.com/bbatsov/rubocop](https://github.com/bbatsov/rubocop)

---

# Workflow

We know that we do not want our changes to diverge too far from the rest of
the group.

> What's the right way to use our source control system to accomplish this
> goal?

There are two popular git-based workflow systems:

* [Git-flow](http://nvie.com/posts/a-successful-git-branching-model/)
* [GitHub Flow](https://guides.github.com/introduction/flow/)

GitHub Flow is simpler and recommended for this class.

---

# GitHub Flow

1. Ensure your master branch is up-to-date with the remote (often called
   `origin`)
2. Create a new branch for your feature (often called a `feature branch`)
3. Make regular
   [atomic commits](https://www.freshconsulting.com/atomic-commits/) to the
   feature branch
4. Regularly push your local changes to the remote branch on github
5. Open a github pull request when the work on the feature branch is complete
6. Have a group member perform a _code review_ of your changes
7. If there are issues to address from _code review_, complete them
8. If there are test failures (you've set up a CI system, right?) fix them
9. Merge the branch to master when everything is good-to-go

__Note__: We neglected the _deploy_ phase just prior to merging.

---

# GitHub Flow Commands

## Ensure your master branch is up-to-date with the remote

    git pull

## Create a new branch for your feature

    git checkout -b feature_name

## Commit to the feature branch regularly

    git add [files...]
    git commit -m "Short useful description of changes."

## Push local changes to the remote

    git push -u origin master

---

# Integration with Git

Recall what we want to reconcile our changes regularly. Feature branches should
be no more than a day or two out-of-sync with their parent branch.

If you want to reconcile your changes without merging to master, a __git
rebase__ is very useful:

    git rebase master feature_branch

![git rebase](img/git_rebase.png)

---

# Git Interactive Rebase

.fx: img-left

![git interactive rebase](img/git_interactive_rebase.png)

If you have been committing frequently and want to squash some commits, consider an interactive rebase:

    git rebase -i master

---

# Pair Programming

.fx: img-left

![Pair programming](img/pair_programming.png)

## Pair Programming

Two developers share one computer and discuss all code that is being written.

## Approaches

### Driver-Navigator

One person does most of the implementation while the other watches, discusses,
thinks of consequences, and looks forward.

### Ping-pong pairing

One person writes the test, the other makes it pass. This approach is
frequently used while learning TDD and pair programming.


In both approaches, pairs should regularly switch roles (e.g., every twenty
minutes).

---

# Pairing: Problem Complexity

![pairing usefulness as a function of problem complexity](img/pairing_and_problem_complexity.png)

Source: Dr. Andrew Mutz

---

# Pairing: Expertise Disparity

![pairing usefulness as a function of expertise_disparity](img/pairing_and_expertise_disparity.png)

Source: Dr. Andrew Mutz

---

# Pairing: Code Reading

![pairing usefulness as a function of amount of time spent reading code](img/pairing_and_code_reading.png)

Source: Dr. Andrew Mutz

---

# Pairing in this class

Pair programming is __strongly__ encouraged, but not required.

When you pair you will inevitably experience more of your project. This means
you can claim you worked on that component in an interview, and as a result
should be able to sufficiently explain what was done.

On the other hand, it is possible for there to be bad pairings among your
group. If you don't feel it is working out, then simply don't do it.

---

# Web HTTP and Application Servers

---

# What does it mean?

After this lecture (will likely continue into Thursday) you should understand
the trade-offs in the following stack descriptions:

## NGINX + Passenger (Recommended for regular testing)

NGINX handles requests to port 80 and passes connections to instances of the
app through Passenger. Multiple concurrent connections are supported.

## Puma

Puma allows both thread-based and process-based
concurrency.


## WEBrick (Use only for slow-performance testing)

WEBrick handles requests to port 80 directly, permitting only a single
connection at a time.

---

# Motivation

We all should have a reasonable understanding of the HTTP protocol.

Many browsers and clients exist that are able to:

* Open a TCP socket
* Send an HTTP request
* Have the request processed
* Receive the data in a response
* Reuse the socket for multiple requests

The software systems that handle the request are generally divided into two
parts:

* HTTP Servers
* Application Servers

---

# Separation of Responsibilities

> Why not use a single process to handle both the http request and the
> application logic?

The two components have separate concerns and design goals.

## HTTP Server

* Provides a high performance HTTP implementation (handles concurrency)
* Extremely stable, and relatively static
* Very configurable and language/framework agnostic

## Application Server

* Written to support a specific language (e.g., Ruby), which may
  hinder performance
* Contains _business logic_ and is extremely dynamic
* Focus on optimizing human resources via abstractions (e.g.,
  model-view-controller [MVC] framework)

---

# HTTP Servers

![Netcraft survey of HTTP servers](img/netcraft_web_servers.png)

Latest:
[https://news.netcraft.com/archives/2016/09/19/september-2016-web-server-survey.html](https://news.netcraft.com/archives/2016/09/19/september-2016-web-server-survey.html)

---

# HTTP Server Responsibilities

* Parse HTTP requests and craft HTTP responses _very_ fast
* Dispatch to the appropriate handler and return response
* Be stable and secure (lots of string parsing)
* Provide clean abstraction for backing applications

>  How do web servers provide concurrency?

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

# TDD, CI, Pairing, and Web/Application Servers
.fx: title

__CS290B__

Dr. Bryce Boe

October 6, 2015

---

# Today's Agenda

* TODO
* Agile Review
* Test Driven Development
* Continuous Integration
* Pair Programming
* Web Servers
* Application Servers

---

# TO-DO

## Before Thursday's Class:

* Read
  [Dynamic Load Balancing on Web-server Systems](http://www.ics.uci.edu/~cs230/reading/DLB.pdf)
  by Cardellini, Colajanni, and Yu.
* Complete through chapter 8 in Agile Web Development with Rails
* Learn git:
  [http://rogerdudler.github.io/git-guide/](http://rogerdudler.github.io/git-guide/)

## By End of Thursday's Lab:

* Add member names and photo to project's README on github
* Create team project on pivotal tracker and add me (bryce.boe@appfolio.com) as
  me as collaborator

---

# Agile Review

> ## Sprint 2: Starts October 15

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
      # test_divisible_by_3 passes
      # test_divisible_by_5 passes
    end

---

# Test FizzBuzz (red)

## Test

    !ruby
    def test_divisisble_by_both
      assert_equal 'FizzBuzz', fizzbuzz(15)
    end

## Program

    !ruby
    def fizzbuzz(n)
      if n % 3 == 0
        'Fizz'
      else
        'Buzz'
      # test_divisible_by_3 passes
      # test_divisible_by_5 passes
      # test_divisible_by_both fails
    end

---

# Test FizzBuzz (green)

## Test

    !ruby
    def test_divisisble_by_both
      assert_equal 'FizzBuzz', fizzbuzz(15)
    end

## Program

    !ruby
    def fizzbuzz(n)
      if n % 3 == 0
        'Fizz'
        if n % 5 == 0
          'Buzz'
        end
      else
        'Buzz'
      # test_divisible_by_3 passes
      # test_divisible_by_5 passes
      # test_divisible_by_both passes
    end

---

# Test Other (red)

## Test

    !ruby
    def test_divisisble_by_neither
      assert_equal 17, fizzbuzz(17)
    end

## Program

    !ruby
    def fizzbuzz(n)
      if n % 3 == 0
        'Fizz'
        if n % 5 == 0
          'Buzz'
        end
      else
        'Buzz'
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
        'Fizz'
        if n % 5 == 0
          'Buzz'
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

* Controller tests
* Integration tests
* Selenium tests

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

If we never let our changes diverage too much from the restof the group,
reconciling our changes will never be too hard.

__Conclusion__: commit early and often, and merge others' changes early and
often

> How do we ensure we have soccessfully reconciled?

---

# Continuous Integration

__Automated Tests!__

Utilize a __Continuous Integration__ server (CI) that will monitor changes to
your source code.

Whenever anyone checks in new code, run all the tests.

* The sonner you find and fix integration problems, the better.
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
testing phase. Integrates with github and travis ci and can be configured to
_fail_ pull requests that decrease code coverage.

[https://coveralls.io/](https://coveralls.io/)

Free for open source projects.

## Rubocop

A static analysis tool for ruby that suggests source code improvements
encompassing code style, unused variables, visually ambiguous statements, and
more.

[https://github.com/bbatsov/rubocop](https://github.com/bbatsov/rubocop)

---


---
layout: default
navigation_weight: 2
permalink: /project/
title: Course Project
---

# Course Project

## Objective

The goal of the project is to gain hands-on experience in building and
deploying a scalable web service on the Internet. Using the latest web
technologies while learning how to tackle the scalability and fault-tolerance
concerns. This is a "learn by doing" course: the course project will form the
primary focus of the course with the lectures and discussion of research papers
providing background material. Each project will be conducted in an agile team
where students will build their own scalable, redundant web site using
fundamental web technologies and the Ruby on Rails framework.


## Getting Started

* Complete chapter 1 in the
  [Ruby on Rails Tutorial](https://www.railstutorial.org/book/beginning)
* Read the list of [project ideas](/project_ideas/).
* Add your own project suggestions.

## Project Sprint Schedule

All sprints end and begin with each week's lab session.

#### Sprint 0: September 27, 2018 -- October 2, 2018
* Install [Rails](http://rubyonrails.org/).
* Learn [Ruby](https://www.ruby-lang.org/en/).
* Complete [Lear Ruby Codecademy](https://www.codecademy.com/learn/learn-ruby).
* Complete chapter 1 in the
  [Ruby on Rails Tutorial](https://www.railstutorial.org/book/beginning).
* Begin chapter 2 in the
  [Ruby on Rails Tutorial](https://www.railstutorial.org/book/toy_app).
* Form your team.

#### Sprint 1: October 2, 2018 -- October 9, 2018
* Complete Chapters 2 through 6 in the Ruby on Rails Tutorial.
* Determine your team's project, get approved by instructor.
* Learn [git](http://rogerdudler.github.io/git-guide/).
* Create and push the base rails application to your team's github repository.

#### Sprint 2: October 9, 2018 -- October 16, 2018
* Complete chapters 7 through 10 in the Ruby on Rails Tutorial.
* Learn TDD: get [Travis CI](http://docs.travis-ci.com) working with your
  github repository.
* Start writing stories for your project in Github projects.
* Decide on a sprint commitment.
* Learn pair programming through pairing up on the first few stories.

#### Sprint 3: October 16, 2018 -- October 23, 2018
* Complete chapters 13 and 14 in the Ruby on Rails Tutorial.
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint.

#### Sprint 4: October 23, 2018 -- October 30, 2018
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint.
* Learn EC2 and Amazon Web Console by deploying your initial application on
  Amazon EC2

#### Sprint 5: October 30, 2018 -- November 6, 2018
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint. Your application should be mostly
  feature complete at this time and subsequent work should focus on polish.
* Define the "critical paths" through your application (the set of pages that a
  common user will go through).

#### Sprint 6: November 6, 2018 -- November 13, 2018
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint. Your application should be feature
  complete at this time and subsequent work should focus on polish.
* Deploy a tsung instance on EC2.
* Write an initial tsung xml file to load test a simple action on your
  application.
* Write a tsung xml file to exercise this critical path.
* Load test your application with tsung running on a m3.medium instance.
* Produce an initial set of graphs with your application's performance.
* Test (and document) the effects of vertical scaling on your application with
  the critical path xml file.
* Deploy and test your application on a variety of load-balanced
  configurations, with the medium--large dataset.
* Test using Tsung, measure, and document.

#### Sprint 7: November 13, 2018 -- November 20, 2018
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint. Only polish is appropriate at this
  point.
* By the end of this sprint your project should be feature complete.
* Create a medium--large dataset (~10,000+ records) using database seeds.
* Test (and document) the effects of horizontal scaling on your application
  with the critical path xml file.

#### Sprint 8: November 20, 2018 -- November 27, 2018
* Conduct a retrospective on how the last sprint went and how you can improve.
* Create a large dataset (more than 100,000 records).
* Inspect and optimize the way your application is interacting with the
  database. If necessary, write custom sql to optimize.
* Implement server-side caching (if you haven't already)
* Deploy your caching optimizations on a simple load-balanced configuration,
  with the large dataset, both with and without memcache.
* Continue testing using Tsung, measure, and document.
* How many users can you handle?

#### Sprint 9: November 27, 2018 -- December 4, 2018
* Conduct a retrospective on how the last sprint went and how you can improve.
* If appropriate, create as large of a dataset as possible. How big can it be?
* Continue testing using Tsung, measure, and document.
* How many users can you handle?
* Complete the project write-up (due Thursday, December 6).
* Prepare final presentation (present Monday, December 10).

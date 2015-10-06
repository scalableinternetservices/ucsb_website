---
layout: default
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

* Follow Chapter 1 of the book (Agile Web Development with Rails 4) for
  installation instructions of Rails for Windows, Mac, or Linux.
* Read the list of [project ideas](/project_ideas/).
* Add your own project suggestions.

## Project Sprint Schedule

All sprints end and begin with each week's lab session.

#### Sprint -1: September 24, 2015 -- October 1, 2015
* Install [Rails](http://rubyonrails.org/).
* Learn [Ruby](https://www.ruby-lang.org/en/).
* Complete [Ruby Code Academy](http://www.codecademy.com/en/tracks/ruby).
* Form your team.

#### Sprint 0: October 1, 2015 -- October 8, 2015
* Read Chapters 1 through 8 in Agile Web Development with Rails.
* Determine your team's project, get approved by instructor.
* Learn [git](http://rogerdudler.github.io/git-guide/).

#### Sprint 1: October 8, 2015 -- October 15, 2015
* Read chapters 9 through 17 in Agile Web Development with Rails.
* Create and push the base rails application to your team's github repository.
* Learn TDD: get [Travis CI](http://docs.travis-ci.com) working with your
  github repository.
* Start writing stories for your project in pivotal tracker.
* Decide on a sprint commitment.
* Learn pair programming through pairing up on the first few stories.

#### Sprint 2: October 15, 2015 -- October 22, 2015
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint.
* Learn EC2 and Amazon Web Console by deploying your initial application on
  Amazon EC2.

#### Sprint 3: October 22, 2015 -- October 29, 2015
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint.
* Deploy a tsung instance on EC2.
* Write an initial tsung xml file to load test a simple action on your
  application.
* Load test your application with tsung running on a micro instance.

#### Sprint 4: October 29, 2015 -- November 5, 2015
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint.
* Define the "critical path" through your application (the set of pages that a
  common user will go through).
* Write a tsung xml file to exercise this critical path.
* Test (and document) the effects of vertical scaling on your application with
  the new critical path xml file.
* Create a medium--large dataset (~10,000 records) using database seeds.
* Perform the vertical scaling tests against your dataset.

#### Sprint 5: November 5, 2015 -- November 19, 2015
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint. Your application should be mostly
  feature complete at this time and subsequent work should focus on polish.
* Deploy your application on a variety of load-balanced configurations, with
  the medium--large dataset.
* Test using Tsung, measure, and document.

#### Sprint 6: November 19, 2015 -- November 26, 2015
* Conduct a retrospective on how the last sprint went and how you can improve.
* Decide on a sprint commitment.
* Implement stories from the current sprint. Only polish is appropriate at this
  point.
* By the end of this sprint your project should be feature complete.
* Inspect and optimize the way your application is interacting with the
  database. If necessary, write custom sql to optimize.
* Deploy your data-related optimizations on a simple load-balanced
  configuration, with the medium--large dataset.
* Test using Tsung, measure, and document.

#### Sprint 7: November 26, 2015 -- December 3, 2015 (No lab on the 26th)
* Conduct a retrospective on how the last sprint went and how you can improve.
* Create a large dataset (more than 100,000 records).
* Implement server-side caching.
* Deploy your caching optimizations on a simple load-balanced configuration,
  with the large dataset, both with and without memcache.
* Test using Tsung, measure, and document.


#### Sprint 8: December 3, 2015 -- December 10, 2015
* Conduct a retrospective on how the last sprint went and how you can improve.
* Complete the project write-up (due December 8).
* Prepare final presentation (present December 10).

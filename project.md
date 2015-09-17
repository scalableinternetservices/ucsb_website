---
layout: default
permalink: /project/
title: Course Project
---

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
* Read the list of [project suggestions](#project_ideas).
* Add your own project suggestions

## Spring 2015 (UCLA) Projects
* [Reddit-style quote sharing website](https://github.com/scalableinternetservicesarchive/Quotopia)
* [An Uber for Anything](https://github.com/scalableinternetservicesarchive/victorious-Secret)
* [Visual voting for events](https://github.com/scalableinternetservicesarchive/Fantastic4)
* [Yikyak meets Snapchat](https://github.com/scalableinternetservicesarchive/U1F44D)
* [Online clothing and merchandise hub](https://github.com/scalableinternetservicesarchive/Atticus)
* [Virtual waiting in line](https://github.com/scalableinternetservicesarchive/Team1024)
* [Gift exchange coordination system](https://github.com/scalableinternetservicesarchive/GiftHub)
* [Gathering activities](https://github.com/scalableinternetservicesarchive/ScalableMaster)
* [Test bank for UCLA](https://github.com/scalableinternetservicesarchive/Gattlestar-Balactica)
* [Univeristy admission application service](https://github.com/scalableinternetservicesarchive/RubyCoders)
* [Multiplayer gaming platform](https://github.com/scalableinternetservicesarchive/yam)
* [Music sharing website](https://github.com/scalableinternetservicesarchive/Michelangelo)
* [Yelp for places](https://github.com/scalableinternetservicesarchive/Yeap)
* [Musical instrument marketplace](https://github.com/scalableinternetservicesarchive/Arpeggio)
* [Find events around you](https://github.com/scalableinternetservicesarchive/whatsup)
* [A location-based note taking application](https://github.com/scalableinternetservicesarchive/MapKeep)
* [Renting and borrowing books](https://github.com/scalableinternetservicesarchive/AirBooks)
* [Food review, discount and discussion application](https://github.com/scalableinternetservicesarchive/Newbie)
* [Delegate tasks as quests](https://github.com/scalableinternetservicesarchive/Questing-Adventurer)

## Fall 2014 (UCSB) Projects

* [An electronic cabin guest book](https://github.com/scalableinternetservices/Team-Hytta)
* [A competition tracking application](https://github.com/scalableinternetservices/Compete)
* [A scalable automatic grading system](https://github.com/scalableinternetservices/Gradr)
* [Find and compare nearby surf spots](https://github.com/scalableinternetservices/BaconWindshield)
* [Find parties near you and share yours](https://github.com/scalableinternetservices/Xup)
* [Questmaster: gamification of everyday tasks](https://github.com/scalableinternetservices/Motley-Crew)
* [Send photos to strangers, and upvote/downvote them](https://github.com/scalableinternetservices/Picshare)
* [Share programming projects like MIT's Scratch](https://github.com/scalableinternetservices/LaPlaya)
* [Suppr: share meals with friends](https://github.com/scalableinternetservices/Suppr)
* [Upload and share viral videos](https://github.com/scalableinternetservices/Upvid)

## <a name="project_ideas"></a>Project Ideas

* Embrace the sharing economy! Build a time-sharing app for pets. Own 30% of a
  dog.
* Government data project. A system that uses the large amounts of data at
  [data.gov](http://data.gov) or the
  [Amazon public data sets](http://aws.amazon.com/publicdatasets/), see the
  [sunlight foundation](http://sunlightfoundation.com/projects/) projects for
  some ideas.
* Leverage the data from the
  [New York Times Developer APIs](http://developer.nytimes.com/docs) in order
  to build something interesting. They have APIs convering geography, movie
  reviews and more.
* Stock trade advisor. A system that gathers information about stocks, stock
  trades, and companies from both traditional and non-traditional sources
  (blogs, email lists, twitter feeds, facebook) and computes interesting
  data. Potential interesting data would be correlations between stock price
  and both non-traditional data, trending information based on non-traditional
  sources. Could also include social aspects for submitting sources, voting for
  impact of source, etc.
* YCombinator inspired:
  [YC Request for Startups](http://www.ycombinator.com/rfs/) Implement some
  portion of one of the YCombinator "Startup ideas we would like to fund"


## Project Sprint Schedule

All sprints end and begin with each week's lab session.

#### Sprint -1: September 24, 2015 -- October 1, 2015
* Install [Rails](http://rubyonrails.org/).
* Learn [Ruby](https://www.ruby-lang.org/en/).
* Complete [Ruby Code Academy](http://www.codecademy.com/en/tracks/ruby).
* Read Chapters 1 through 8 in Agile Web Development with Rails.
* Form your team.

#### Sprint 0: October 1, 2015 -- October 8, 2015
* Determine your team's project, get approved by instructor.
* Read chapters 9 through 17 in Agile Web Development with Rails.
* Learn [git](http://rogerdudler.github.io/git-guide/).

#### Sprint 1: October 8, 2015 -- October 15, 2015
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

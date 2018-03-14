---
layout: default
---

## Course Description

This course explores advanced topics in highly scalable Internet services and
their underlying systems architecture. Software today is increasingly being
delivered as a service: accessible globally via web browsers and mobile
applications and backed by millions of servers. Modern frameworks and platforms
are making it easier to build and deploy these systems, such as
[Ruby on Rails](http://rubyonrails.org/) and
[Amazon's EC2](https://aws.amazon.com/ec2/).

Yet despite these advances, some concerns just don't go away. Building scalable
Internet services today still requires an understanding of topics like caching,
load balancing, security, and monitoring. In this course we will examine these
topics and more: the state of the art in building scalable Internet services.

## Lectures

Course lectures will be Tuesdays and Thursdays, from 1:00pm to 2:50pm in
Phelps 2510. Lecture material will cover the essentials of building large scale
Internet services. The lecture schedule and slides are available online.

## Project

The goal of the course project is to gain hands-on experience in building and
deploying a scalable web service on the Internet. Students will do this using
some of the latest web technologies in order to learn how to tackle scalability
and fault-tolerance concerns. Projects will be conducted in agile teams of five
students, and team will build their own scalable web site using fundamental web
technologies and the [Ruby on Rails](http://rubyonrails.org/) framework.

Project-centric lab will meet every DAYOFWEEK from START:00pm to END:00pm in
Phelps 3525. These mandatory labs offer a chance to collaborate with your
teammates, demo your progress to the instructor, and get guidance.

## Learning Outcomes

By the end of this course CS291A students will be able to:

* create a [Ruby on Rails](http://rubyonrails.org/) web service and deploy it
  to [Amazon's EC2](https://aws.amazon.com/ec2/)
* detail a significant majority of the general _services_ and protocols that
  are, or may be, involved when browsing to a high-traffic volume web service
  such as [reddit.com](https://www.reddit.com)
* determine via measurement where bottlenecks exist in a web service under
  their control
* employ memcached to reduce the load on an uncached web service in order to
  handle a larger volume of traffic
* utilize git to contribute to open source projects on
  [github](https://github.com/) via pull requests

## Grading

At the end of the quarter each group's project will be assigned a grade based
on their web service being of sufficient complexity, and the group's
description of their methodological approach to load testing and subsequent
scaling via various techniques as described in their project write-up and/or in
their project presentation. Objectively these components break down into:

* 30%: web service complexity
* 50%: load testing and scaling (communicated through presentation and/or
  write-up)
* 10%: quality of project presentation
* 10%: quality project write-up

On an individual basis, 5% of one's grade is based on their
participation in-class and on piazza.

The remaining 95% of an individual's grade will be computed by multiplying
their group's project grade by an individual score. Individual scores are
computed by suming the relative percent of _work_ each individual
confidentially assigns other individuals in their group.

For example, given a three person group with a group grade of 95%, everyone
individually with 100% participation, and the following peer-graded scores:

|           | Alice     | Bob      | Chuck     |
|:---------:|:---------:|:--------:|:---------:|
| Alice     | -         | 55%      | 45%       |
| Bob       | 60%       | -        | 40%       |
| Chuck     | 52%       | 48%      | -         |
|===========|===========|==========|===========|
| __Total__ | __112%__  | __103%__ | __85%__   |
{: class="table table-striped"}

Then Alice would end with a 106.4% (A+), Bob with 97.85% (A+) and Chuck with
80.75% (B-).

So that everyone knows where they stand within their group, we will
confidentially conduct the peer grading process three times during the course
(November 2, November 21, and December 7). Only the outcome of the final
peer-grade (December 7) will be used to compute the final grade.

### Letter Grades

Letter grades will be assigned as follows:

| Percent | Grade |
|:-------:|:------|
|   96 ⅔  |   A+  |
|   93 ⅓  |   A   |
|   90    |   A-  |
|   86 ⅔  |   B+  |
|   83 ⅓  |   B   |
|   80    |   B-  |
|   76 ⅔  |   C+  |
|   73 ⅓  |   C   |
|    0    |   F   |
{: class="table table-striped"}

The number listed is the lower bound of the percent grade for the given
range. It is expected that you are a relatively equal contributor in your
group, with adjustments for significant positive outliers. Thus, please take
note of the drop directly from C to F.

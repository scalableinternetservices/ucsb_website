---
layout: default
---

## Course Description

This course explores advanced topics in highly scalable Internet services and
their underlying systems architecture. Software today is primarily delivered as
a service: accessible globally via web browsers and mobile applications and
backed by millions of servers. Modern web frameworks (e.g., [Ruby on
Rails](http://rubyonrails.org/), [Django](https://www.djangoproject.com), and
[Express](https://expressjs.com)), and continuous improvements to cloud
providers (e.g., [Amazon Web Services](https://aws.amazon.com), [Google Cloud
Platform](https://cloud.google.com), and [Microsoft
Azure](https://azure.microsoft.com/en-us/)) make it increasingly easier to
build and deploy these systems.

Despite these advances, building scalable Internet services today still requires
an understanding of topics like caching, load balancing, security, and
monitoring. In this course we will examine these topics and more: the state of
the art in building scalable Internet services.


## Learning Outcomes

By the end of this course students will be able to:

* write and deploy highly scalable web functions using [AWS
  Lambda](https://aws.amazon.com/lambda/)

* create and deploy [Docker](https://www.docker.com/get-started) containers
  using [Google's Cloud Run](https://cloud.google.com/run/)

* write a modern front end client application using [React](https://reactjs.org)

* create a [Ruby on Rails](http://rubyonrails.org/) web service and deploy it
  via [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)

* measure the performance of various components of a web service

* discover and resolve bottlenecks in a web service


## Lectures

Lecture material will cover the essentials of building large scale Internet
services. The lecture schedule and slides are available online at
[https://cs291.com](https://cs291.com). Lecture attendance is optional, but
strongly recommended as interactive examples will be provided during lecture
that often won't be well reflected in the online material.

## Labs

Mandatory labs will meet once a week in Phelps 3525. These labs offer students
a chance to collaborate on their projects and demo progress on the primary
project.

## Initial Projects

There will be four projects in the first five weeks of the course, one per week
with the fourth project spanning two weeks. These projects will ensure students
have the basic knowledge to build and deploy modern, simple, and scalable web
services without needing a deep understanding of how the underlying systems
enable scalability. The first three projects are to be completed individually,
and the fourth completed in a pair.

## Primary Project

The goal of the course's primary project is for students to experience and
resolve pain points encountered when building and deploying a moderate-sized
scalable web service. Students will do this using some of the latest web
technologies in order to learn how to tackle scalability and fault-tolerance
concerns. Projects will be conducted in agile teams of four students, and each
team will build their own scalable web site using fundamental web technologies
and the [Ruby on Rails](http://rubyonrails.org/) framework.


## Grading

| Percent | Item |
|--:|:--|
| 3 | [Project 0](project0) (Static Web Page) |
| 6 | [Project 1](project1) (AWS Lambda) |
| 9 | [Project 2](project2) (Google's Cloud Run) |
| 12 | [Project 3](project3) (Chat Server and Client) |
| 65 | [Primary Project](project) Individual Grade |
| 5 | Participation |
{: class="table table-striped"}

Participation can be earned by asking or answering questions during lectures,
and asking or answering public questions on Piazza.

Projects 0 through 3 are scored as either complete (`100%`) or incomplete (`0%`);
there is no fractional score.

Late submissions incur a `1%` penalty for every minute late rounded up to the
nearest minute. For example, if the deadline is `13:59:59`, an assignment
submitted at `14:00:00` will receive `99%` of its score, and an assignment
submitted at `15:00:00` will receive only `39%` of its score.

### Primary Project Scoring

At the end of the quarter each group's project will be assigned a score based
on their web service being of sufficient complexity, and the group's
description of their methodological approach to load testing and subsequent
scaling via various techniques as described in their project write-up and/or in
their project presentation. Objectively these components break down into:

| Percent | Item |
|--:|:--|
| 50 | load testing and scaling (communicated through presentation and/or write-up) |
| 30 | web service complexity |
| 10 | quality of project presentation |
| 10 | quality of project write-up |
{: class="table table-striped"}

### Primary Project Individual Grading

The project individual grade is computed by multiplying a student's group's
project score by their individual project score. Individual project scores are
computed by summing the relative percent of _work_ each individual's teammates
confidentially assigns them.

For example, given a three person group with a group grade of 95% and the
following peer-graded scores:

|           | Alice     | Bob      | Chuck     |
|:---------:|:---------:|:--------:|:---------:|
| Alice     | -         | 55%      | 45%       |
| Bob       | 60%       | -        | 40%       |
| Chuck     | 52%       | 48%      | -         |
|===========|===========|==========|===========|
| __Total__ | __112%__  | __103%__ | __85%__   |
{: class="table table-striped"}

Then Alice's Primary Project Individual Grade would be `106.4%`, Bob with
`97.85%` and Chuck with `80.75%`.

We will confidentially conduct the peer grading process twice during the
course. Only the outcome of the second peer-grade (on the day of presentations)
will be used to compute the final grade.

Any moderate deviations from near-equal grades will require discussion.

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

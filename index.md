---
layout: default
---

Note: This page is still being updated for Winter 2021. Its content is subject to change.
{: .alert .alert-info }

## Course Description

This course explores advanced topics in highly scalable Internet services and
their underlying systems' architecture. Software today is primarily delivered as
a service: accessible globally via web browsers and mobile applications, and
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


## Class Content and Interactions


### Pre-recorded Videos

All core course topics, covering the essentials of building large scale
Internet services, will be presented in the form of pre-recorded videos. Links
to the videos and associated material for each topic should be made available
at the beginning of the week the topic is covered.


### Synchronous Classes

Class will meet twice a week during the scheduled class time unless otherwise
mentioned. Students are expected to watch the week's videos prior to the
scheduled class times in order to leverage the class time to ask and answer
questions, and explore the material in more depth.

These classes will be held via Zoom. The Zoom classes will be recorded and
shared only with enrolled students. Students are strongly encouraged, but not
required, to turn on their web cameras when speaking and interacting in
break-out rooms with their peers.

Should the instructor experience any technical difficulties during synchronous
classes, students may check Piazza for updates.

Should a student experience any technical difficulties during synchronous
classes, they can visit the [LSIT Help Center](https://help.lsit.ucsb.edu/hc/en-us),
or they can send an email to <help@collaborate.ucsb.edu>.

<div class="well">
Please read the following UCSB notice regarding class Zoom recordings:

> This live Zoom session will be recorded for students who may not be able to
> attend at this time. By default, your microphone and camera will be muted
> when you join the session. If you do not want to be included in the
> recording, simply keep your camera and microphone off. You may ask questions
> in the chat window. NOTE: Student participants are prohibited from recording
> of any kind. Only the instructor is permitted to record.

Source: <https://keepteaching.id.ucsb.edu/?page_id=113>
</div>

## Piazza

...

## Nectir

...

### Team Check-ins

Once the primary project has started in week 5, teams will meet with the
instructor once each week, via Zoom. These meetings will be scheduled for
approximately 15 minutes.

## Projects

### Initial Projects

There will be four projects in the first five weeks of the course, one per week
with the fourth project spanning two weeks. These projects will ensure students
have the basic knowledge to build and deploy modern, simple, and scalable web
services without needing a deep understanding of how the underlying systems
enable scalability. The first three projects are to be completed individually,
and the fourth completed in a pair.

### Primary Project

The goal of the course's primary project is for students to experience and
resolve pain points encountered when building and deploying a moderate-sized
scalable web service. Students will do this using some of the latest web
technologies in order to learn how to tackle scalability and fault-tolerance
concerns. Projects will be conducted in agile teams of four to six students,
and each team will build their own scalable web site using fundamental web
technologies and the [Ruby on Rails](http://rubyonrails.org/) framework. A team
may not be comprised of more than two undergraduate or BS/MS students.


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

Participation is an important part of keeping a class engaging. Participation
can be earned by asking or answering questions during synchronous classes, and
asking or answering public questions on Piazza. Note that neither private
conversations with the instructor, nor participation during team check-ins
count toward the participation score.

Projects 0 through 3 are scored as either complete (`100%`) or incomplete (`0%`);
there is no fractional score other as described below for late submissions.

Late submissions incur a `1%` penalty for every five-minutes late rounded up.
For example, if the deadline is `13:59:59`, an assignment submitted at
`14:00:00` (5 minutes late) will receive `99%` of its score, and an assignment
submitted at `15:00:00` (65 minutes late) will receive only `87%` of its score.

### Primary Project Scoring

At the end of the quarter each team's project will be assigned a score based
on their web service being of sufficient complexity, and the team's
description of their methodological approach to load testing and subsequent
scaling via various techniques as described in their project report and in
their project presentation. Objectively these components break down into:

| Percent | Item |
|--:|:--|
| 60 | load testing and scaling (communicated through presentation video and report) |
| 20 | web service complexity |
| 10 | quality of project presentation video |
| 10 | quality of project report |
{: class="table table-striped"}

### Primary Project Individual Grading

The project individual grade is computed by multiplying a student's team's
project score by their individual project score. Individual project scores are
computed by summing the relative percent of _work_ each individual's teammates
confidentially assigns them.

For example, given a three person team with a team grade of 95% and the
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
range. It is expected that each person is a relatively equal contributor on
their team, with adjustments for significant positive outliers. Thus, please
take note of the drop directly from C to F.

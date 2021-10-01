---
layout: default
---
# Scalable Internet Services Syllabus

## Course Description

This course explores advanced topics in highly scalable Internet services and
their underlying systems' architecture. Software today is primarily delivered
as a service: accessible globally via web browsers and mobile applications, and
backed by millions of servers. Modern web frameworks (e.g., [Ruby on
Rails](http://rubyonrails.org/), [Django](https://www.djangoproject.com), and
[Express](https://expressjs.com)), and continuous improvements to cloud
providers (e.g., [Amazon Web Services](https://aws.amazon.com), [Google Cloud
Platform](https://cloud.google.com), and [Microsoft
Azure](https://azure.microsoft.com/en-us/)) make it increasingly easier to
build and deploy these systems.

Despite these advances, building scalable Internet services today still
requires an understanding of topics like caching, load balancing, security, and
monitoring. In this course we will examine these topics and more: the state of
the art in building scalable Internet services.

## Learning Outcomes

By the end of this course students will be able to:

- write and deploy highly scalable web functions using [AWS
  Lambda](https://aws.amazon.com/lambda/)

- create and deploy [Docker](https://www.docker.com/get-started) containers
  using [Google's Cloud Run](https://cloud.google.com/run/)

- write a modern front end client application using
  [React](https://reactjs.org)

- create a [Ruby on Rails](http://rubyonrails.org/) web service and deploy it
  via [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)

- measure the performance of various components of a web service

- discover and resolve bottlenecks in a web service

## Class Content and Interactions

### Synchronous Classes

All core course topics, covering the essentials of building large scale
Internet services, will be presented via in-person lectures.

Class will meet twice a week during the scheduled class time unless otherwise
mentioned. Students are encouraged to attend in order to ask and answer
questions, and explore the material in more depth.

### Piazza

All students are expected to join the class on Piazza as class announcements
will be made there. Additionally Piazza is used for offline questions about the
class content and its projects. Students are able to submit anonymously, though
anonymous content will not be counted toward participation. Students are
strongly encouraged to answer each other's questions by improving upon the
"student answer".

Please create a new post for each distinct question, rather than asking new
questions as a follow up to an existing post. Follow-ups are useful to obtain
more information necessary to answer a question, or to work through possible
solutions to a question.

All one-on-one offline communication with the instructors for content
pertaining to this class should be conducted via Piazza. Please do not reach
out to the instructor via email for class related communications.

### Team Check-ins

Once the primary project has started in week 5, teams will meet with either
Bryce or Nevena once each week, via Zoom. These meetings will be scheduled for
approximately 15 minutes.

## Projects

### Initial Projects

There will be four projects in the first five weeks of the course, one per week
with the fourth project spanning two weeks. These projects will ensure students
have the basic knowledge to build and deploy modern, simple, and scalable web
services without needing a deep understanding of how the underlying systems
enable scalability. The first three projects are to be completed individually,
and the fourth completed as a pair.

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
| 3 | [Project 0](/project0/) (Static Web Page) |
| 6 | [Project 1](/project1/) (AWS Lambda) |
| 9 | [Project 2](/project2/) (Google's Cloud Run) |
| 12 | [Project 3](/project3/) (Chat Server and Client) |
| 65 | [Primary Project](/project/) Individual Score |
| 5 | Participation |
{: class="table table-striped"}

Participation is an important part of keeping a class engaging. Participation
can be earned by asking or answering questions during synchronous classes, and
asking or answering public questions on Piazza. Note that neither private
conversations with the instructor, nor participation during team check-ins
count toward the participation score.

Projects 0 through 3 are scored as either complete (`100%`) or incomplete
(`0%`); there is no fractional score other than as described below for late
submissions.

Late submissions incur a `1%` penalty for every five-minutes late rounded up.
For example, if the deadline is before `2pm`, an assignment submitted at
`14:00:00` (5 minutes late) will receive `99%` of its score, and an assignment
submitted at `15:00:00` (65 minutes late) will receive only `87%` of its score.

### Primary Project Score

A project's score is primarily based on the team's description of their
iterative approach to load testing and scaling their web service as described
in their project report and highlighted in their project video. Objectively
these components break down into:

| Percent | Item |
|--:|:--|
| 60 | iterative approach to load testing and scaling
| 20 | web service complexity |
| 10 | quality of project report |
| 10 | quality of project video |
{: class="table table-striped"}

### Primary Project Individual Score

The individual score is computed by multiplying the project score by the
student's peer score. Peer scores are computed by summing the relative percent
of _work_ each individual's teammates confidentially assigns them.

For example, a three person team may assign the following peer scores:

|           | Alice     | Bob      | Chuck     |
|:---------:|:---------:|:--------:|:---------:|
| Alice     | -         | 55%      | 45%       |
| Bob       | 60%       | -        | 40%       |
| Chuck     | 52%       | 48%      | -         |
|===========|===========|==========|===========|
| __Total__ | __112%__  | __103%__ | __85%__   |
{: class="table table-striped"}

The observations from the data in the table above are:

- Alice reported Bob (`55%`) as having contributed more work than Chuck
  (`45%`).
- Similarly, Bob reported that Alice (`60%`) contributed more work than Chuck
  (`40%`).
- Finally, Chuck reported that Alice (`52%`) contributed slightly more work
  than Bob (`48%`).

With these values, Alice's peer score would be `112%`, Bob's `103%`, and
Chuck's `85%`. With a project score of `95%`, Alice's Primary Project
Individual Score would be `106.4%`, Bob's `97.85%`, and Chuck's `80.75%`.

We will confidentially conduct the peer score process twice during the course:

- Monday, November 8
- Monday, November 22

The first two peer scores are intended to help students see if they need to
make any adjustments to their team contributions. Only the outcome of the final
peer score will be used to compute an individual's score. Any moderate
deviations of more than two points from equal contribution will require
justification, and may be followed up on by the instructor.

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
their team, with the exception that there may be significant positive
outliers. Additionally, it is expected that each team does a solid job on their
project. As a result, please note the drop to an `F` grade immediately
following the `C` range.

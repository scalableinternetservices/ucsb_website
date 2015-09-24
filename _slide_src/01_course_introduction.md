# Course Introduction
.fx: title

__CS290B__

Dr. Bryce Boe  
(Bryce is preferred)

September 24, 2015


---


# Welcome to CS290B

Please grab an index card and write:

* Your name
* Your email address
* Your education level and year (e.g., 2nd year MS)
* Your prior experience with Internet technology
* What you hope to get from this class


---


# About Me

* UCSB CS Alum (BS: 2008, Ph.D.: 2014)
* As a graduate student:
    * Taught 3 undergraduate CS courses
    * TAed for numerous other courses
* Took this course in Winter 2009 (CS290N at the time)
* Senior Software Engineer @ AppFolio
* Assisted with the Fall 2014 course
* 13+ years of web "development" experience
    * Learned HTML in 1996
    * Learned PHP & MySQL around 2002


---


# My Teammates "Pear" Programming

![Jon and Adam 'Pear' Programming](img/pear_programming.png)


---


# Today's Agenda

* Course Overview
    * Course Motivation
    * Course Structure
    * Course Grading
* The Lifecycle of a Web Request
    * Group Exercise
    * Review


---


# Pull requests, pull requests, pull requests!

![Pull Requests! Pull Requests! Pull Requests!](img/developersdevelopers.gif)

If you notice an issue with or wish to make an improvement to any of the course
content (e.g., slides, web pages) please edit them and make a pull request.

Website source:  
[https://github.com/scalableinternetservices/ucsb_website/](https://github.com/scalableinternetservices/ucsb_website/)

Slide source:  
[https://github.com/scalableinternetservices/ucsb_website/tree/master/slides](https://github.com/scalableinternetservices/ucsb_website/tree/master/slides)


---


# Questions and Feedback

At any point during this course:

Stop me to:

* ask a question
* ask for clarification
* provide an additional example

Communicate to me:

* how I can help you succeed in this course
* ideas for making the course more engaging
* any other feedback you may have


---


# Course Motivation


---


# Thought Experiment #1

How do you find a place to rent?


---


# Thought Experiment #1

* [Rent.com](http://www.rent.com/)
* [Apartment Guide](http://www.apartmentguide.com/)
* [Rental Houses](http://www.rentalhouses.com/search/Goleta-CA)
* [Zillow](http://www.zillow.com/homes/for_rent/)
* [Realtor](http://www.realtor.com/apartments/Goleta_CA)
* [Trulia](http://www.trulia.com/for_rent/Goleta,CA)
* [PadMapper](http://www.padmapper.com/)


---


# Thought Experiment #2

How do you find your way in a new city?


---


# Thought Experiment #2

* [Google Maps](https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#safe=off&q=map+of+goleta)
* [mapquest](http://www.mapquest.com/maps?city=Goleta&state=CA)
* [tripadvisor](http://www.tripadvisor.com/LocalMaps-g32438-Goleta-Area.html)
* [Yelp](http://www.yelp.com/c/goleta-ca-us/restaurants)


---

# Thought Experiment #3


How do you find someone to date?


---


# Thought Experiment #3


* [Zoosk](https://www.zoosk.com/)
* [Match](http://www.match.com/)
* [OurTime](http://www.ourtime.com/)
* [Elite Singles](http://dating.elitesingles.com/)
* [Christian Mingle](http://www.christianmingle.com/)
* [JDate](http://www.jdate.com/)
* [SingleParentMeet](http://www.singleparentmeet.com/)
* [OkCupid](https://www.okcupid.com/)
* [Tinder](https://www.gotinder.com/)


---


# Internet (or Web) Services!

Each of the problems can be solved by a variety of Internet services.

Every day billions of people use various Internet services to solve problems
like these.

As an Internet service grows in popularity, supporting the increased amount of
Internet traffic results in increased complexity of the Internet service.


---


# Internet Services, what's that?

![Question Mark](img/question_mark.jpg)


---


# Internet Services, what's that?

There are many application-level protocols that could be used to build out an
Internet Service.

For this class Internet services will refer to HTTP-based services.

The interface to your web service may be the web browser (e.g., Chrome,
Firefox), a REST-based API, or both.


---


# What about mobile?

 We will discuss some optimizations
 ([HPBN chapter 5](http://chimera.labs.oreilly.com/books/1230000000545/ch05.html))
 designed for mobile users.

Many native mobile apps are backed by Internet services via an API.

![Mobile v. Desktop from 2010 through 2014](img/mobile_v_desktop.png)


---


# Scalable, what does that mean?

![Question Mark](img/question_mark.jpg)


---


# Scalable, what does that mean?

An Internet service is scalable if increasing demands can be effectively met
with increasing capacity.

Demands could be:

* Web traffic quantity (typical association)
* Dataset size


---


# Effectively meet demands: Explanation

* Internet service remains available
* Response time does not excessively degrade

## Think about it

Assume you have a web service designed to run on a single server with a plan to
use a bigger server when it can no longer effectively meet demand.

__Is this scalable?__


---


# What you will do:

In this course you will learn and utilize some of the technologies behind
building large-scale Internet services.

You will test and support to the best of your abilities one or more of:

* Expontential growth in the amount of traffic to your web service
* Expontential growth in the dataset your web service relies upon


---


# In Summary

This course won't teach you how to build a web application that obtains
worldwide attention and usage.

However, this course will teach you how to build a web application __that can
respond to__ worldwide attention and usage.


---

# Other Topics

In addition to scaling, we will learn about:

* Performance
* Security
* Agile software development
* Test driven development
* Web clients (e.g., web browsers)


---


# TODO

## By next class

* Join the class on [Piazza](https://piazza.com/class/idgkoaxbvg14lx)
* Read chapters 1 and 2 in
  [High Performance Browser Networking](http://chimera.labs.oreilly.com/books/1230000000545/ch01.html)
* Read the list of project ideas: [http://cs290.com/project_ideas/](http://cs290.com/project_ideas/)
* Post or comment on at least one idea on Piazza under the `project_idea`
  "folder"
* Start Learning Ruby (begin
  [Ruby Code Academy](https://www.codecademy.com/tracks/ruby))

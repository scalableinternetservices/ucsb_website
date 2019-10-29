---
layout: default
navigation_weight: 10
permalink: /project/
title: Primary Project
---

# Primary Project

Below is an approximate schedule for the primary project. As the quarter
progresses it'll become more complete.

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

- Complete chapter 1 in the
  [Ruby on Rails Tutorial](https://www.learnenough.com/ruby-on-rails-4th-edition-tutorial/beginning)

## Project Sprint Schedule

All sprints end and begin with each week's lab session, save for the last
sprint which does not have an ending lab session.

At the end of each sprint during lab section, you will need to do the
following:

- Ensure all your completed stories are integrated on your master branch.
- Deploy your project using Elastic Beanstalk.
- Demo your deployed version and share the newly created features.
- Share any new load testing results.


#### Sprint 1: October 29 -- November 5

- Complete {{ site.codecademy_md_link }}.
- Form your team.
  - Decide on a team name
  - One person on the team, message me on piazza with:
    - Your team name
    - The name, and github username of all the team members
- Get access to your github respository (I'll create that after the above)
- Get a new set of AWS credentials specific to your team.
- Deploy your initial rails code to Elastic Beanstalk.
- Complete `N` user stories, where `N` is the number of people on your team.
- Write a tsung load test encompassing your existing features.
  - Ensure that when it is run, there are no 4XX or 5XX level HTTP status
    codes.

#### Sprint 2: November 5 -- November 12

#### Sprint 3: November 12 -- November 19

#### Sprint 4: November 19 -- November 26

#### Sprint 5: November 26 -- December 3

#### Sprint 6: December 3 -- December 6 (short sprint)

- Complete the project write-up (due Friday, December 6 by 19:59:59 PST).
- Prepare final presentation (present Thursday, December 12 between 4PM and
  7PM).


## Project Ideas

Please select from one of the following project ideas. You are free to modify
them as you wish, and can even come up with another project idea, but the
complexity must remain the same.

Please note all the user stories start off with unauthenticated users. That's
because you want to deliver functionality first. Implementing authentication
first does not provide any value, if that authentication has no features behind
it. Complete a set of unauthenticated stories first, prior to introducing
authentication.

### Social Network

Minimum necessary models:

- Post
- Comment (on Post)
- Profile
- Message (profile to profile)

Initial user stories:

0. As an unauthenticated user I can make a post so that I can share whatever
   cool things I want.

0. As an unauthenticated user I can view all the posts on the front page in
   descending order so that I can see what new things people are sharing.

0. As an unauthenticated user, I can comment on a post so that I can add
   updates to existing content.

0. As an authenticated user, my front page shows only posts made on my profile
   so that I can see content specific to me.

0. As as authenicated user, my posts and comments are attributable to me so
   that others know what I've shared.


### Online Store

Minimum necessary models:

- Item
- Order
- Rating (user to item)
- User

Initial user stories:

0. As an unauthenticated user I can list my item on the store so that I can
   sell my products.

0. As an unauthenticated user I can purchase an item from the store so that I
   can obtain the things I desire.

0. As an unauthenticated user I can view all the purchase histories so that I
   can see what others have bought.

0. As an unauthenticated user, I can rate an item that has been purchased so
   that I can share my opinions of the item with others.

0. As an authenticated user, only I can see my own orders in my order history
   because I don't want others to see what I've purchased.


### Event Sharing Service

Minimum necessary models:

- Event
- RSVP
- Comment
- User
- Invite

Initial user stories:


0. As an unauthenticated user, I can create an event so that I can share with
   others the details of the event I am hosting.

0. As an unauthenticated user, I can comment on an event to share my enthusiasm
   for said event.

0. As an authenticated user, I can RSVP yes/no to events that I do [not] indend
   to attend so that the host can better estimate how many people will show up.

0. As an authenticated user, I can see the list of events that I have
   previously attended so that I can recall my fond memories.

0. As an event host, I can proactively invite users to my event, so that I can help spread the word.

---
layout: default
navigation_weight: 5
permalink: /project3/
title: Project 3
---

# Project 3: Demo Rails App

In this project you will learn how to setup a basic Ruby on Rails app.
The app will be a small twitter-like app with the list of users who can create
new posts and comment on the existing posts. One user will have many posts, and
one post can have many comments. Each comment belongs to the user and the post.

## Learning Outcomes

- Student was able to create a functional RoR app

- Student used MVC pattern to create three interconnected resources

- Student has implemented CRUD operations

- Student demonstrated the app and its functionality in a 3min video

## Project Submission

Submission: <{{site.project3_submission}}>

Pairing message: <{{site.project3_team_message}}>

## List of supported endpoints

- Navigating to the `/users` endpoint will list all `users` in your app

- Navigating to the `/users/:id` will show the page with the information
  about the `user` with the given `id`

  - Returns 404 if the id was not found.

- From the browser, you can create the user

- From the browser, you can update the user

- From the browser, you can delete the user

- There is a validation error for incorrect create or update action

  - E.g. Each user has to have an email and an error is displayed if this required
    value is not provided

- Users index page (`/users`) shows the list of all the users; for each user it shows
  the list of all posts that belong to the given user and for each post
  it shows all the comments that belong to the post.

## Resources

[Ruby on Rails Guides](https://guides.rubyonrails.org/)

[The Ruby On Rails Tutorial](https://www.railstutorial.org/book)  
_[Complete 3rd edition available online](https://3rd-edition.railstutorial.org/book)_

[MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

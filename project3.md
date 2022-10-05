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

<{{site.project3_submission}}>

## List of supported endpoints

Each one of the three supported resources enables CRUD operations

- Navigating to the `/posts` endpoint will list all `posts` in your app

- Navigating to the `/posts/:id` will show the page with the information
about the `post` with the given `id`

  - Returns 404 if the id was not found.

- From the browser, you can update the post

- From the browser, you can delete the post

- From the browser, you can create the post
  - Each post has to have a user and an error is displayed if this required
  value is not provided

- `/users` and `/comments` support the same set of operations.

- A user's page shows the list of all posts that belong to the given user

- A post's page shows the list of all of its comments

## Resources

[Ruby on Rails Guides](https://guides.rubyonrails.org/)

[The Ruby On Rails Tutorial](https://www.railstutorial.org/book)  
_[Complete 3rd edition available online](https://3rd-edition.railstutorial.org/book)_ 

[MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
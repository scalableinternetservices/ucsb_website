# Project 3: Demo Rails App

In this project you will learn how to setup a basic Ruby on Rails app.
The app will be a small twitter-like app with the list of users who can create
new posts and comment on the existing posts. One user will have many posts, and
one post can have many comments. Each comment belongs to the user and the post.

## Learning Outcomes

- Student was able to create a functional RoR app

- Optional (Student was able to use React for the front end in combination with RoR backend)

- Student used MVC pattern to create three interconnected resources

- Student has implemented CRUD operations

- Student demonstrated the app and its functionality in a 3min video

## Project Submission

{% if site.project3_team_message and site.project3_submission %}
- [Team message]({{site.project3_team_message}})

- [Submission]({{site.project3_submission}})
{% else %}

- Submission link will be posted at start of quarter

{% endif %}

## List of supported endpoints

- Navigating to `/login` will provide you with a simple form where you can enter
  your username.  No password is required.  When you submit the login form a new
  user should be created if no user matches the username or an exiting user should
  be logged in if the username exists.  Either way, you should be re-directed to
  the root of the application `/`.  This should initialized a user session and
  store the identity of the user in the session.

- Navigating to `/logout` should remove the user information from the session

- Navigating to any page other than `/login` without a user session should result
  in a re-direct to `/login`

- Navigating to the root of the application `/` when you are logged in will show
  a list of all the posts from all users in chrolological order with the most
  recently created post at the top.  Each post should include:
  - The content of the post
  - The username of the user who created the post
  - The number of comments on a post (linkable to `/posts/:id` described below)
  - The time the post was last updated
  - (Not Required) - Consider adding a search filter form input that allows you to
    filter the list of posts to just those for the specified username

- Navigating to the `/posts/:id` will show the page with the information
  about the `post` with the given `id` including
  - The content of the post
  - The author of the post
  - The list of comments for the post
  - A form to add a new comment to a post.  Submitting this form should
    show keep the browser on the same page but show the newly posted comment

  - Returns 404 if the id was not found.

- From the browser, you can create a post

- From the browser, you can update a post but only if you are the author

- From the browser, you can delete a post but only if you are the author

- From the browser, you can comment on any post

- There should be a validation error for posts or comments that are attempting to influence the election.
  Have fun with this.  A simple example might be a validation error for posts that include
  the words "Trump" or "Harris"

## React Considerations

Using React is optional.

If you plan to do a React front end for your application, you may want to create
an API implementation for your controller actions. See [Rails API-only application guide](https://guides.rubyonrails.org/api_app.html).
The main difference would be that your RoR controller actions would likely take JSON as input
and return JSON as output.  All or at least some of applications UI would be implemented
in javascript using React rather than using Rails views.

## Resources

[Ruby on Rails Guides](https://guides.rubyonrails.org/)

[The Ruby On Rails Tutorial](https://www.railstutorial.org/book)  
_[Complete 3rd edition available online](https://3rd-edition.railstutorial.org/book)_

[MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

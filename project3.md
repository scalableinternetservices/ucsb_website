---
layout: default
navigation_weight: 5
permalink: /project3/
title: Project 3
---

# Project 3: Chat Server and Corresponding React Front-End

In this project you will write a chat server using sinatra and packaged in a
docker container, as well as a standalone React-based front-end for your chat
sever.

Your front-end should have the capability to seamlessly work with both your
server, and my deployed version of the server. Similarly my deployed front-end
should be able to seamlessly interact with your server.


## Working in Pairs (optional)

This project is significantly more complex than the previous projects. You will
need to maintain state in your Sinatra application, and many of you will learn
entirely new framework, React. I estimate this project to be more than four
times the work of [Project 2](/project2/). As a result, this project spans two
weeks, and you have the option of working with another student of the course.

If you are to work in a pair, please have one member of your pair send a
private message on Piazza to `instructors` and include your pair in the `to`
indicating that the two of you will work together. Once you've formed a pair,
you and your partner are committing to stick with the pairing.

If you intend to work solo, please also message `instructors` on Piazza to
indicate your choice to work solo. You may later pair up with someone by the
pairing deadline.

The pairing deadline is: Tuesday October 22, 10:59:59 AM PDT.


## Due Date

Tuesday October 29, 10:59:59 AM PDT


## Learning Outcomes:

Coming soon.


## Project Submission

Coming soon.


## Resources

### Hosted Server Example

[http://chat.cs291.com/](http://chat.cs291.com/)

The application at the above URL contains a complete server implementation
which your client should be able to communicate with. Of course, the server
side code will not be provided as it's up to you to replicate its
functionality.

### Client Example

While the above link also serves a complete client, it's more interesting to
have a client hosted on a different domain as the interaction then requires
CORS. A copy of the client, with CSS and JavaScript separated can be found at:

[https://cs291.com/project3/chat/](https://cs291.com/project3/chat/)

And, while you can view the source in the browser, it might be more convenient
to see it on GitHub:

[https://github.com/scalableinternetservices/ucsb_website/tree/master/project3/chat](https://github.com/scalableinternetservices/ucsb_website/tree/master/project3/chat)

__Note__: The logic of this client is written 100% in JavaScript and as such it
serves as a poor example of code to copy since you can better accomplish the
same with React. While you may end up writing more code when using React, the
maintainability of the React code is significantly greater, especially when
accompanied with component unit tests.


## Required Tools

* [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (Cors)

* [Docker](https://www.docker.com/products/docker-desktop)

* [JSX](https://reactjs.org/docs/introducing-jsx.html)

* JavaScript [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)

* [React](https://reactjs.org)

* [Server-Sent Events](https://www.w3.org/TR/eventsource/)

* [Sinatra](http://sinatrarb.com/)


## Suggested Reading

* [Server-Sent Events (SSE)](https://hpbn.co/server-sent-events-sse/) in High Performance Browser Networking

* [XMLHttpRequest](https://hpbn.co/xmlhttprequest/) in High Performance Browser Networking

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
server, and my deployed version of the server (reference server). Similarly my
deployed front-end (reference client) should be able to seamlessly interact
with your server.


## Working in Pairs (optional)

This project is significantly more complex than the previous projects. You will
need to maintain state in your Sinatra application, and many of you will learn
an entirely new framework, React. I estimate this project to be more than four
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


## Learning Outcomes

* Student has written and deployed a React application coded using JSX.

* Student has added CORS headers to their web application to support
  third-party front-ends.

* Student has leveraged Server-Sent Events and Javascript's EventSource to
  provide a real-time communication platform.


## Project Submission

Coming soon.


## HTTP API Specification

The following endpoints are the only required endpoints. Feel free to add more
endpoints or more functionality so long as the reference client continues to
work with your server. Sections indicated via `(reference)` are not required,
but are listed so you understand why the reference server behaves a certain
way.

__Note__: I've intentionally excluded any CORS related headers and endpoints
from the following list.

### POST /login

This endpoint is used to grant a user an access token. In the reference
implementation, the endpoint is also used to immediately register a new
user. Once a user has been created, they must login with the same password.

Returns:

* `201` with the JSON body `{"token": <SIGNED TOKEN>}` on success

* `403` if the provided `username` and `password` combination doesn't match
  that of an existing user

* `422` if either `password` or `username` is blank

* (reference) `422` if the set of provided fields do not exactly match the
  expected fields

Expected Form Fields:

* `password`
* `username`

__WARNING__: Do not send real passwords to this system. The reference server is
not protected by TLS and thus all data sent to or from the server is
unencrypted.

Example curl command:

```sh
curl -D- <BASE_URL>/login -F username=<USERNAME> -F password=<PASSWORD>
```

Example HTTP response:

```
HTTP/1.1 201 CREATED
Content-Type: application/json

{"token": "<SIGNED TOKEN>"}
```

### POST /message

Send a message to all users of the chat system.

Returns:

* `201` on success

* `403` if `<SIGNED TOKEN>` is not valid

* `422` if `message` is blank

* (reference) `422` if the set of provided fields do not exactly match the
  expected fields

Expected Headers:

* `Authorization` with value `Bearer <SIGNED TOKEN>`

Expected Form Fields:

* `message`: a string of the message to send

Example curl command:

```sh
curl -D- <BASE_URL>/message -F message=test \
-H "Authorization: Bearer <SIGNED TOKEN>"
```

Example HTTP response:

```
HTTP/1.1 201 CREATED
```


### GET /stream/<SIGNED TOKEN>

Returns:

* `200` and begins the Server-Sent Event stream with events as described the
  following section

* `403` if `<SIGNED TOKEN>` is not valid

Example curl command:


```sh
curl -D- <BASE_URL>/stream/<SIGNED TOKEN>
```

Example (partial) HTTP response:

```
HTTP/1.1 200 OK
Content-Type: text/event-stream; charset=utf-8

data: {"users": ["curl"], "created": 1570999219.797813}
event: Users
id: 0718299d-43ef-4b1c-b1cf-ba828d195959

data: {"status": "Server start", "created": 1570947584.0895946}
event: ServerStatus
id: ed4e3e63-9680-436d-9ab2-e0546b5cc03f

data: {"message": "We're online!", "user": "bboe", "created": 1570947655.5598643}
event: Message
id: 1a72e044-92e4-4ee5-94fe-5cabacb75b83
```


## SSE Events

Below are a list of events that you must support and implement. The `data`
field of all events must be JSON. All events have a unique ID which is included
as part of the SSE protocal, and not part of the `data` attribute.

### Disconnect

Indicates that the server is closing the connection. The browser must not
auto-retry on disconnect.

Fields:

* `created` (float): the unix timestamp when the event was created

### Join

Indicates that a user has joined the chat.

Fields:

* `created` (float): the unix timestamp when the event was created
* `user` (string): the username of the user who joined the chat

### Message

Represents a message from a user connected to the chat.

Fields:

* `created` (float): the unix timestamp when the event was created
* `message` (string): the message from the user
* `user` (string): the username of the sender

### Part

Indicates that a user has left the chat.

Fields:

* `created` (float): the unix timestamp when the event was created
* `user` (string): the username of the user who left the chat

### ServerStatus

Used for the server to provide status updates.

Fields:

* `created` (float): the unix timestamp when the event was created
* `status` (string): the message from the server

### Users

Provides a complete list of users connected to the chat server. This message is
always sent out on connection of new streams.

Fields:

* `created` (float): the unix timestamp when the event was created
* `users` (array[string]): the list of connected users


## React Front-end Specification

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

* [Server-Sent Events](https://www.w3.org/TR/eventsource/) (SSE)

* [Sinatra](http://sinatrarb.com/)


## Suggested Reading

* [Server-Sent Events (SSE)](https://hpbn.co/server-sent-events-sse/) in High Performance Browser Networking

* [XMLHttpRequest](https://hpbn.co/xmlhttprequest/) in High Performance Browser Networking

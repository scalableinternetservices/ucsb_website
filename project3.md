---
layout: default
navigation_weight: 5
permalink: /project3/
title: Project 3
---

# Project 3: Chat Server and Corresponding React Front-End

In this project you will write a chat server using the Sinatra framework, as
well as a stand-alone React front-end for your chat sever. The server will be
packaged into a Docker container.

Your front-end should have the capability to seamlessly work with both your
server, and my deployed version of the server (reference server). Similarly my
deployed front-end (reference client) should be able to seamlessly interact
with your server.

---

## Working in Pairs (optional)

This project is significantly more complex than the previous projects. You will
need to maintain state in your Sinatra application, and many of you will learn
an entirely new framework, React. I estimate this project to be more than four
times the work of [Project 2](/project2/). As a result, this project spans two
weeks, and you have the option of working with another student of the course.

If you will work in a pair, please have one member of your pair send a private
message to me on Piazza with both members' names to indicate that the two of
you will work together. Once you've formed a pair, you and your partner are
committing to stick with the pairing.

If you intend to work solo, please also message me on Piazza to indicate your
choice to work solo. Should you change your mind, you may later pair up with
someone by the pairing deadline.

The pairing deadline is listed in the side bar.

---

## Learning Outcomes

- Student has written and deployed a React application coded using JSX.

- Student has added CORS headers to their web application to support
  third-party front-ends.

- Student has leveraged Server-Sent Events and JavaScript's EventSource to
  provide a real-time communication platform.

---

## Overview Video

<https://youtu.be/FutR00lpAfE>

Note: This video is for a former version of this project. The specification has
slightly changed.

---

## Template Project

Please create a new private repository from this template:

<https://github.com/scalableinternetservices/cs291a_project3_template/generate>

---

## Project Submission

Please have each team member submit the following form:

<https://forms.gle/RUyjZxor1U9JzGuA9>

### Deliverables

In order to submit the form you will need three additional things:

- The name of a pushed docker container that when invoked runs your chat
  server, e.g., `us.gcr.io/cs291a/project3_YOURNAME`

- A URL to your deployed front-end application with minimized JavaScript (tip:
  `yarn build`).

- A URL to your GitHub repository. Assuming this repository is `private`,
  please invite me, `bboe` on GitHub so that I can see your code.

__Note__: Please do not deploy this project to Google Cloud Run. First, it
won't work as expected because Google Cloud Run has a maximum connection
timeout. Second, I will run your docker containers locally.
{: .alert .alert-danger }

---

## HTTP API Specification

You will need to implement the following endpoints for this project.

__Note__: I've intentionally excluded any CORS related headers and endpoints
from the following list. It's up to you to determine the necessary CORs
endpoints.
{: .alert .alert-warning }

### POST /login

This endpoint is used to grant a user an access token. The endpoint is also
used to immediately register a new user. Once a user has been created, they
must login with the same password. The server should store the user
registrations in memory.

Returns:

- `201` with the JSON body `{"message_token": <SIGNED MESSAGE TOKEN>,
  "stream_token": <SIGNED STREAM TOKEN>}` on success. The server should
  invalidate any previous `message_token` and `stream_token` values assigned to
  the user, resulting in new tokens for each succesful login. No other `/login`
  response status code should reset the tokens.

- `403` if the provided `username` and `password` combination does not match
  that of an existing user

- `409` if there is already a `stream` open for the `username`

- `422` if either `password` or `username` is blank

- `422` if the set of provided fields do not exactly match the two expected
  fields

Expected Request Form Fields:

- `password`: the password associated with `username`
- `username`: the name of the user's account in the system

Example curl command:

```sh
curl -D- <BASE_URL>/login -F username=<USERNAME> -F password=<PASSWORD>
```

Example HTTP response:

```http
HTTP/1.1 201 CREATED
Content-Type: application/json

{"message_token": "<SIGNED MESSAGE TOKEN>", "stream_token": "<SIGNED STREAM TOKEN>"}
```

### POST /message

Send a message to all users of the chat system.

Returns:

- `201` on success. Additionally, the `message_token` value associated with the
  user should be overwritten and the new one returned via the `Token` HTTP
  response header. This action is to ensure each `message_token` may be used
  only once.

- `403` if `<SIGNED MESSAGE TOKEN>` is not valid

- `409` if there is not a `stream` open for the `username` associated with the
  message token. Additionally, the `message_token` value should be rotated in
  the same way as described in `201`.

- `422` if `message` is blank

- `422` if the set of provided fields do not exactly match the expected fields

Expected Request Headers:

- `Authorization` with value `Bearer <SIGNED MESSAGE TOKEN>`

Expected Request Form Fields:

- `message`: a string of the message to send

Example curl command:

```sh
curl -D- <BASE_URL>/message -F message=test -H "Authorization: Bearer <SIGNED MESSAGE TOKEN>"
```

Example HTTP response:

```http
HTTP/1.1 201 CREATED
Token: <NEW SIGNED MESSAGE TOKEN>
```

### GET /stream/&lt;SIGNED STREAM TOKEN&gt;

Returns:

- `200` and begins the `Server-Sent Event` stream with events as described the
  following section

- `403` if `<SIGNED STREAM TOKEN>` is not valid

- `409` if there is already a `stream` open for the `username` associated with
  the stream token

Example curl command:

```sh
curl -D- <BASE_URL>/stream/<SIGNED STREAM TOKEN>
```

Example (partial) HTTP response:

```http
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

<div class="alert alert-info">
__Note__: You might be wondering:

- Why do we pass the stream token in the URL of the request?
- Why do we have two separate tokens?
- Why don't we rotate the stream token, like we do with the message token?

Those are great questions. In a nutshell, `EventSource` does not support
sending arbitrary HTTP headers with the HTTP requests, and it does not support
reading arbitrary HTTP headers from the HTTP response. Additionally the
connection URL cannot be modified after the `EventSource` is created. As a
result we cannot:

1. pass an `Authorization: Bearer <TOKEN>` along with the HTTP request
2. extract a newly generated token from the associated HTTP response
3. rotate the stream token lest we want to break the `EventSource` automatic
   reconnect behavior

</div>

---

## SSE Events

Below are a list of events that you must support and implement. The `data`
field of all events must be JSON. All events have a unique ID which is included
as part of the SSE protocol, and not part of the `data` attribute.

### Disconnect

Indicates that the server is closing the connection. The browser must not
auto-retry on disconnect.

Fields:

- `created` (float): the Unix timestamp when the event was created

### Join

Indicates that a user has joined the chat.

Fields:

- `created` (float): the Unix timestamp when the event was created
- `user` (string): the username of the user who joined the chat

### Message

Represents a message from a user connected to the chat.

Fields:

- `created` (float): the Unix timestamp when the event was created
- `message` (string): the message from the user
- `user` (string): the username of the sender

### Part

Indicates that a user has left the chat.

Fields:

- `created` (float): the Unix timestamp when the event was created
- `user` (string): the username of the user who left the chat

### ServerStatus

Used for the server to provide status updates.

Fields:

- `created` (float): the Unix timestamp when the event was created
- `status` (string): the message from the server

### Users

Provides a complete list of users connected to the chat server. This message is
only sent out on connection of new streams and not on reconnect where the
`Last-Event-Id` header would be present.

Fields:

- `created` (float): the Unix timestamp when the event was created
- `users` (array[string]): the list of connected users

## Server Requirements

- Your server must maintain state about the users who are connected.

- A broadcast `JOIN` should be made any time a user has connected.

- A broadcast `PART` should be made any time a user has disconnected.

- A `Users` event should be sent to each new stream (i.e., not reconnects).

- Incoming messages should be broadcast to everyone.

- A `Disconnect` should be sent to a user who messages `/quit`. Their `POST
  /stream/<TOKEN>` HTTP response should then be closed by the server.

- The first event in the server should be `ServerStatus` indicating the server
  has started.

- A history of at least the last 100 broadcast events should be kept.

- All of the `Message` or `ServerStatus` in the history should be sent to a
  newly connecting user (`JOIN` and `PART` events should not be sent to a newly
  connecting user).

- A user who is reestablishing its connection (retry after failure) should
  receive all of the messages in the history that have occurred since the
  provided `Last-Event-Id` header value. If the value of `Last-Event-Id` is not
  found in the history, then the connection should be treated as a new
  connection.

---

## Server Commands

The following `/` commands should be implmented by your server via the `POST
/messages` endpoint.

### /kick &lt;USERNAME&gt;

Like `/reconnect`, but applied to the user respresented by `USERNAME`. If there
is no connected user associated with `USERNAME`, or a user tries to kick
themselves, the `POST /message` HTTP response status should be `409`. Because
no `DISCONNECT` event is sent, the kicked user's client's `EventSource`
instance should automatically reconnect to the server.

### /quit

Messages a `DISCONNECT` to the sending user, broadcasts a `PART` for that user,
and ends their HTTP `stream`. The client should not attempt to reconnect.

### /reconnect

Broadcasts a `PART` for the sending user and ends their HTTP `stream`. Because
no `DISCONNECT` event is sent, the client's `EventSource` instance should
automatically reconnect to the server.

---

## React Front-end Specification

Your application need not be anything like the reference application. It
however, must meet the following requirements:

- Connection status should be visually discernible between being connected and
  disconnected.

- There should be an easy way to see who is connected.

- There should be a way to discover when someone connected (`JOIN`).

- It should be easy to discover when someone disconnected (`PART`).

- New `Message` events should be immediately apparent.

- `ServerStatus` events should be discoverable.

- For retry-able connection failures (e.g., `/reconnect`, `/kick`), your
  application should automatically reconnect (`EventSource` should handle this
  for you).

- On `Disconnect` your application should not automatically attempt to
  reconnect to the server.

- A user should always be able to take an action (e.g., connect, send
  message). In other words there should be no client state that requires a page
  refresh.

- Separate browser windows and/or tabs should each be able to have their own
  connection to the server.

### Components

While the names do not need to be the same, you need to at least implement the
following React components:

- Compose (a way to input / send a message)
- LoginForm
- MessageList
- UserList

---

## Developing React Using Docker

The following instructions are not necessary, but might make it easier if you
don't want to set up the dependencies on your machine.

### Clone your copy of the project 3 template repository

Make sure you've make a copy of the [template
repository](./#template-project). Then run:

```sh
git clone <YOUR_REPO_URI>
cd <YOUR_REPO_DIRECTORY>
```

### Run the react development server

Change into the `client` directory and start the Docker container by running:

```sh
cd client
docker run -it --rm -p 3000:3000 -v $(pwd):/app -w /app node /bin/bash
```

The above maps local port `3000` to container port `3000`. Synchronizes the
contents of the current local directory with `/app` in the container, and
starts up `bash`.

Once in bash, start up the development server:

```sh
cd chat_client
yarn start
```

Once started, you should be able to access your application via:
<http://localhost:3000>

This template React client will try to establish a trivial `EventSource`
connection to <http://localhost:3001> in order to interact with the template
server (view the JavaScript console to see a message on connection).

### Make Changes

Locally, edit the contents of files under `client` and when you save, you
should see said changes automatically take effect in the browser without
needing to refresh.

### React Tutorial

Follow this guide to add more components:
<https://reactjs.org/docs/hello-world.html>

---

## Running the Template Server

In a different terminal, change into the `server` directory and then build the
template container:

```sh
cd server
docker build -t us.gcr.io/cs291a/project3_${CS291_ACCOUNT} .
```

Then start the the container:

```sh
docker run -it -p 3001:3000 --name server --net cs291 --rm us.gcr.io/cs291a/project3_${CS291_ACCOUNT}
```

Note: Ensure you've run `docker network create cs291` before running the above.

Note that `thin` runs on container port 3000, but so does webpacker. Thus we'll
map host port 3001 to the container port 3000.

---

## Resources

### Hosted Server Example

<https://chat.cs291.com/>

The application at the above URL contains a complete server implementation
which your client should be able to communicate with. Of course, the server
side code will not be provided as it's up to you to replicate its
functionality.

### Client Example

While the above link also serves a complete client, it's more interesting to
have a client hosted on a different domain as the interaction then requires
CORS. A copy of the client, with CSS and JavaScript separated can be found at:

<https://cs291.com/project3/chat/>

And, while you can view the source in the browser, it might be more convenient
to see it on GitHub:

<https://github.com/scalableinternetservices/ucsb_website/tree/main/project3/chat>

__Note__: The logic of this client is written 100% in JavaScript and as such it
serves as a poor example of code to copy since you can better accomplish the
same with React. While you may end up writing more code when using React, the
maintainability of the React code is significantly greater, especially when
accompanied with component unit tests.
{: .alert .alert-warning }

---

## Required Tools

- [Cross-Origin Resource
  Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS)

- [Docker](https://www.docker.com/products/docker-desktop)

- [JSX](https://reactjs.org/docs/introducing-jsx.html)

- JavaScript [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)

- [React](https://reactjs.org)

- [Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html) (SSE)

- [Sinatra](http://sinatrarb.com/)

---

## Suggested Reading

- [Server-Sent Events (SSE)](https://hpbn.co/server-sent-events-sse/) in High
  Performance Browser Networking

- [XMLHttpRequest](https://hpbn.co/xmlhttprequest/) in High Performance Browser Networking

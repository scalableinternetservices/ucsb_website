# HTTP and HTML
.fx: title

__CS290B__

Dr. Bryce Boe

September 29, 2015

---

# Today's Agenda

* TODO
* The Life Cycle of a Web Request
* HTTP
* HTML
* Intro to CSS

---

# TO-DO

## Before Thursday's Class:

* Join the class on [Piazza](https://piazza.com/class/idgkoaxbvg14lx)
* Read chapters 1 and 2 in
  [High Performance Browser Networking](http://chimera.labs.oreilly.com/books/1230000000545/ch01.html)
* Read the list of project ideas: [http://cs290.com/project_ideas/](http://cs290.com/project_ideas/)
* Post or comment on at least one idea on Piazza under the `project_idea`
  "folder"
* Start Learning Ruby (begin
  [Ruby Code Academy](https://www.codecademy.com/tracks/ruby))

---

# The Life Cycle of a Web Request

---

# Review: The Two Endpoint Basics

A web browser is a process (at least one) that runs on an operating system. It:

* responds to user input
* renders the display
* utilizes the network

A web server is a process (at least one) that runs on an operating system. It:

* responds to network requests
* loads resources that may come from file system, database, other servers

---

# Core Components of a Web request

* Web server: Opens a TCP socket to listen for requests
* Browser: Makes a DNS query to obtain an IP address for www.reddit.com
* Browser: Establishes a TCP connection to the IP address
* Web server: Accept the TCP connection
* Web server: Add TLS context to the TCP connection
* Browser: Wraps a TLS session on-top of the TCP connection
* Browser: Sends an HTTP request over the TLS session
* Web server: Parse the request, fetch and send the requested resources

---

# HTTP

---

# Chrome Network Table

By the end of today's lecture, you should understand this output:

![Chrome Network Table](img/chrome_network_table.png)

---

# History

The year is 1990. The Internet has exisited for ~20 years, email for ~8.

Tim Berners-Lee has the idea to combine __HyperText__ and the __Internet__. He
creates the first version of __HTTP__ and __HTML__.

__HyperText__: Links documents together via __HyperLinks__

* 1993: Mosaic, the first web browser, is created at UIUC
* 1994: Marc Andreessen leaves UIUC and founds Netscape with Jim Clark

---

# The First Web Server

![The First Web Server](img/first_web_server.png)

---

# HTTP Explained

It its original, simplest version:

* Open a TCP socket (standard port is 80)
* Send an ASCII request for a resource (`GET mypage.html`)
* Response comes back containing only the content of `mypage.html`
* Close the TCP socket

HTTP was originally designed to:

* Send HTML (was later extended to send anything)
* To facilitate interaction between a web browser and a web server (now also
  used heavily for server-to-server communication)

---

# HTTP Request/Response Components

## HTTP Request

* __Verb__: What do you want to do (e.g., __GET__, __POST__)
* __Resource__: What is the logical path of the resource you want
* __HTTP Version__: What version of HTTP are you using?
* __Headers__: Standard way to specify or request optional behavior
* __Body__: Content that is being sent to the server (e.g., a file upload)

## HTTP Response

* __HTTP Version__: Indicates the HTTP version the server is "speaking"
* __Status Code__: Indicates success, failure, or other possible response
  states
* __Headers__: Provides meta data about the response.
* __Body__: The primary payload of the response (for a successful _GET_
request, this contains the resource content)

---

# HTTP Components Example

![Components of HTTP request and response](img/http_components.png)

---

# HTTP Verbs GET and POST

## GET

* Request a copy of a _resource_
* The request should have no side-effects (i.e., doesn't change server state)
* __GOOD__: `GET /fluffy_kitty.jpg`
* __BAD__: `GET /users/sign_out`

## POST

* Sends data to the server
* Generally used to create a _resource_
* Has side-effects (e.g., creates a resource)
* Not idempotent (i.e., making the same request twice creates two
  separate, but similar resources)
    * "Do you want to submit your form again?"

---

# HTTP Verbs PUT and DELETE

## PUT

* Sends data to the server
* Often used to update an existing resource
* Has side-effects
* Should be idempotent (e.g., updating a resource twice should result in the
  same effect to the resource)

## DELETE

* Destroys a resource
* Has side effects
* Should be idempotent
* __GOOD__: `DELETE /session/<id>` (for log out)

---

# HTTP Verb HEAD

## HEAD

* Exactly like GET but excludes the body in the response

> What can HTTP HEAD be used for?

---

# HTTP Verb Misuse

Correct HTTP verb usage is not enforced, and is often misused.

> What do you think the following is supposed to do?

`GET /post/5?action=hide`

> What other problem do you think can occur with the misuse of HTTP verbs?

---

# Other HTTP Verbs

* TRACE
* OPTIONS
* CONNECT

---

# HTTP Resource

Specifies a logical hierarchy to access a resource:

__GOOD__: /gp/product/1565925092/
__BAD__: /index.jsp?page_id=4251

## Query String

* The portion of the resource after the _question mark_
* Used to assist in locating the resource
* Values are assigned using the equal token (e.g., `id=15`)
* Multiple values can be concatenated via ampersand (`&`)

Example:

http://www.reddit.com/r/ucsantabarbara/?__sort=new&t=all__

---

# HTTP Version

Version strings are often used in protocols to make it easy to evole the
protocol.

With HTTP different versions have different behavior:

* (1991) HTTP 0.9 (retroactively versioned): Single line protocol with no
  headers. `GET index.html`
* (1996) HTTP 1.0: Added headers, and a version string
* (1999) HTTP 1.1: Connection keep-alive by default, additional caching
  mechanisms. __Primary HTTP version used today__
* (2015) HTTP 2.0: Binary framing, header compression, many other
  optimizations. Discussed in more detail in a future lecture

---

# HTTP Headers

Provides metadata for the request and response.

> What HTTP headers do you know of?


# HTTP Headers: Accept

Indicates the format of the resource

`Accept: text/html`

I desire the resource in html format.

`Accept: application/json`

I desire the resource as a JSON document.

`Accept application/json,application/xml`

I prefer a JSON document, but if you cannot do that then an XML document will
do.

---

# HTTP Headers: Accept-*

## Accept-Encoding

Indicates preferred encoding for the response body.

`Accept-Encoding: bzip2,gzip,`

I prefer the data compressed via bzip2. If that cannot be done, please gzip the
response.

## Accept-Language

Indicates the preferred language for the resource

`Accept-Language: es,en-US`

I prefer spanish, but will accept US-english.

---

# HTTP Headers: Host, User-Agent

## Host (required in HTTP 1.1 request)

Indicates the DNS hostname associated with the desired resource.

> Why is the HOST header required?

## User-Agent

Indicates information about the client (web browser, crawler, tool) to the web
server.

`User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36`

Can be used to serve different content to different clients. However, try to
avoid doing so.

---

# HTTP Headers: Set-Cookie, Cookie

## Set-Cookie

A response header informing the browser to use the provided cookies in
subsequent requests to the server.

## Cookie

A request header containing the data previously set by the server via a
`Set-Cookie` header.

> What kind of information might one put in a cookie?

> What security concerns may exist with cookies?


---

# Other HTTP Headers

## Caching Related Headers

* ETag
* Date
* Last-Modified
* Cache-Control
* Age

## Security Related Headers

* Strict-Transport-Security
* X-Frame-Options
* X-Forwarded-Proto

`X-` prefixed headers are not part of the official specification and may later
become _standardized_.


---

# HTTP Statuses

The HTTP response status indicates the outcome of the request. Status codes
fall into one of five categories:

* 1XX - Informational (e.g., 100 Continue)
* 2XX - Successful (e.g., 200 OK)
* 3XX - Redirection (e.g., 301 Moved Permanently, 304 Not Modified)
* 4XX - Client Error (e.g., 400 Bad Request, 404 Not Found)
* 5XX - Server Error (e.g., 500 Internal Server Error, 505 HTTP Version Not
  Supported)


Ref: [HTTP Status Code Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

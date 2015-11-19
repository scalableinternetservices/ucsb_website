# Clients, JavaScript, and Client-side MVC
.fx: title

__CS290B__

Dr. Bryce Boe

November 19, 2015

---

# Today's Agenda

* Browser Wars
* XMLHttpRequest (AJAX)
* Fast JavaScript
* Client-side MVC
    * Backbone
    * Angular
    * Ember
    * React

---

# Browser Wars

* Mid-90s Nescape reigns supreme
* 1995 - Microsoft releases initial version of Internet Explorer

Competition between Netscape and Microsoft produces significant innovation in
browsers:

* JavaScript
* Cookies
* CSS

---

# Browser Wars

Microsoft bundles Internet Explorer with Windows 98
* Every file management window is a browser
* Results in an antitrust lawsuit against Microsoft

Meanwhile, Netscape focuses on open-sourcing its browser.
* Creates Mozilla Organization
* Is acquired by AOL in 1999
* AOL closes down Netscape division in 2003, and Mozilla Foundation is born.


---

# Browser Market Share

![Browser Market Share to 2009](img/browser_market_share.png)

---

# Innovation Lull

.fx: table-left

| Year |Version|
|------|-------|
| 1995 | IE 1  |
| 1995 | IE 2  |
| 1996 | IE 3  |
| 1997 | IE 4  |
| 1999 | IE 5  |
| 2001 | IE 6  |
| 2006 | IE 7  |
| 2009 | IE 8  |

Microsoft's significant marketshare results in a lack of competition, and a
lull in innovation.

Time between releases increases:

---

# Browser Market Share Shift

Around 2002, Microsoft starts losing market share to Firefox due to:
* Security
* Performance

In 2008 Google announces Chrome.

Browser innovation reignites and today there are 4 popular browsers:

* Internet Explorer
* Chrome
* Firefox
* Safari

---

# Current Global Browser Market Share

![Browser Market Share between 2009 and 2015](img/browser_market_share2.png)

---

# Major Client-side Improvements

* XMLHTTPRequest
* DOM Manipulation
* V8

---

# XMLHttpRequest (AJAX)

Allows JavaScript on the page to asynchronously request resources from the
server.

    !javascript
    var request = new XMLHttpRequest();
    request.onload = function() {
      console.log("I'm a callback!");
    };
    request.open("GET", "/comments", true);
    request.send();

`XMLHttpRequest` was originally added to IE to enable the Outlook Web Access
team to asynchronously communicate between a browser viewing their web page,
and the server hosting the web page (around year 2000).

`XMLHttpRequest` has nothing to do with XML (it can transport XML documents).

`XMLHttpRequest` was a de facto standard by ~2004.


---

# XMLHttpRequest

Prior to the introduction of `XMLHttpRequest`, two-way communication between
the browser and the server required a full page refresh triggers by the click
of a link, or the submission of a form.

`XMLHttpRequest` allows JavaScript that runs in the context of the browser to
send requests and receive responses in whatever way programmed to do so.

For instance, Google shows suggested search terms as you type in your search
phrase.

These days, many developers avoid calling `XMLHttpRequest` directly and use
__jQuery__ instead:

    !javascript
    $.get('/comments', function() { console.log("I'm a callback!"); });

---

# Restricted Headers

For security purposes, `XMLHttpRequest` does not permit the caller from
modifying the following HTTP request headers:

* Accept-Charset, Accept-Encoding, Access-Control-*
* Host
* Upgrade
* Connection
* Referer
* Origin
* Cookie
* ...

---

# Same Origin Policy

An origin is defined as a triple containing _protocol_, _domain_, and _port_
(e.g., `[http, google.com, 80]`).

By default (and the only original option) `XMLHttpRequest`s can only be sent to
the same origin.

The same origin security policy prevents some_malicious_site.com from making
requests to any other site (e.g., gmail) on your behalf.

---

# Cross-Origin Resource Sharing (CORS)

CORS is a protocol that permits the browser to make cross-origin requests for
`GET`, `POST`, and `HEAD` requests.

By default the browser will actually always make the request with the addition
of a `Origin: http://request.origin` header

The browser will only return the response back to JavaScript if the HTTP
response contains a header like:

    Access-Control-Allow-Origin: http://request.origin

While the broswer always issues the requests, it omits the cookies for the
domain, and any HTTP authentication.

---

# CORS with Credentials

To enable cookies and/or HTTP authentication the browser must first ask for
permission from the server.

On the client side the code need only add `xhr.withCredentials = true;`.

    !javascript
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://other.domain/data', true);
    xhr.withCredentials = true;
    xhr.send();

Behind the scenes the browser makes an `OPTIONS` request to other.domain:

    !http
    OPTIONS /data HTTP/1.1
    Host: other.domain
    Origin: http://my.domain
    Access-Control-Request-Method: POST

The browser expects the server to respond with headers like:

    Access-Control-Allow-Origin: http://my.domain
    Access-Control-Allow-Methods: POST

---

# DOM Manipulation

## Document Object Model

The DOM is a standardized way of representing the structure of a web page as a
tree of in-memory objects.

These objects are accessed via JavaScript in order to be queried and
manipulated.

## Example

    !javascript
    var newDiv = document.createElement("div");
    var newContent = document.createTextNode("Hello World!");
    newDiv.appendChild(newContent);
    document.body.appendChild(newDiv);

---

# DOM Manipulation Progression

## (~1995) DOM Level 0: Navigator 2, IE 3

* Allowed reading the values of forms and links
* Not standardized (called legacy DOM)

## (~1998) DOM Level 1: Navigator 4, IE 5

* Allowed access and modification of anything by index

        document.forms[1].elements[2]

## (~2000) DOM Level 2

* Added `getElementById`, DOM event model

## (~2004) DOM Level 3 (current)

* XPath support
* Keyboard event handling

---

# V8: Fast JavaScript

Google releases Chrome in September 2008.

In addition to other novel features (e.g., process per tab), Chrome includes
the V8 JavaScript engine.

V8 applies modern, state-of-the-art virtual machine techniques to JavaScript.
* With V8, JavaScript is not interpreted, but dynamically compiled to machine
  code
    * Re-compiled and re-optimized at runtime
* Garbage collection is fast
    * Generational: separates allowed memory into young and old groups and
      treats them differently
    * Incremental: doesn't need to perform all GC at once
* Other optimizations:
    * Inlining
    * Copy Elision
    * Inline caching

---

# JavaScript VM Wars!

The release of V8 resulted in tremendous performance improvements in other
JavaScript VMs:

* Safari's JavaScriptCore
* IE's Chakra
* Firefox's SpiderMonkey

Today these VMs are all evenly matched. The performance leader frequently
switches, but together they continue to push the boundaries of performance.

__Aside__: V8 was also designed to work outside of the browser. Node.js is
built on top of the V8 engine.

---

# Engine Comparison: Kraken

[http://krakenbenchmark.mozilla.org/](http://krakenbenchmark.mozilla.org/)

* Green: Chrome
* Orange: Firefox

![Kraken Time](img/js_engine_kraken.png)

Source:
[http://arewefastyet.com/#machine=28](http://arewefastyet.com/#machine=28)

---

# Engine Comparison: Octane

[http://chromium.github.io/octane/](http://chromium.github.io/octane/)

* Green: Chrome
* Orange: Firefox

![Octane Time](img/js_engine_octane.png)

Source:
[http://arewefastyet.com/#machine=28](http://arewefastyet.com/#machine=28)

---

# Engine Comparison: Octane

[https://www.webkit.org/perf/sunspider/sunspider.html](https://www.webkit.org/perf/sunspider/sunspider.html)

* Green: Chrome
* Orange: Firefox

![Sunspider Time](img/js_engine_sunspider.png)

Source:
[http://arewefastyet.com/#machine=28](http://arewefastyet.com/#machine=28)

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

* Mid-90s Netscape reigns supreme
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

Microsoft's significant market share results in a lack of competition, and a
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

* XMLHttpRequest
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

While the browser always issues the requests, it omits the cookies for the
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
    * Re-compiled and re-optimized at run time
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

# Engine Comparison: Sunspider

[https://www.webkit.org/perf/sunspider/sunspider.html](https://www.webkit.org/perf/sunspider/sunspider.html)

* Green: Chrome
* Orange: Firefox

![Sunspider Time](img/js_engine_sunspider.png)

Source:
[http://arewefastyet.com/#machine=28](http://arewefastyet.com/#machine=28)

---

# Client-side Renaissance

By 2008, we have all the ingredients ready for a "client-side renaissance". We
have globally installed virtual machines that:

* presents content that can communicate via Ajax to the web service they
  originated from
* have full programmatic control of the user interface (DOM + events)
* use modern, high performance VM techniques
* exist in a competitive marketplace
    * four viable browsers, available on multiple OSes
    * being standards-compliant is a competitive advantage

---

# Modern Client-side Applications

Instead of being a series of pages requested from a web server, we can serve up
a running JavaScript application that:

* regularly sends user input back to the server
* receives structured data rather than rendered markup (JSON instead of HTML)

These applications generally persist through user interactions.

* Clicks no longer necessarily mean full-page refreshes.

Communication with the server is decoupled from user interaction.

* While the browser sits open, a JavaScript timer can trigger a check for new
  data, and update the page as needed.

---

# Consequences of this Shift

* Client side becomes significantly more complex
* Full page refreshes become less common
* Does your application work "offline"?
* How real-time is your application?
* The "running application" is more static and cacheable
* The web server acts more like an API than a web service
* The structured data can be used by mobile applications and other Internet
  services

---

# Demo App: Server-side

In a traditional web application:

* When you click the "New Submission" button, the browser makes a HTTP request,
and loads the response.

* The response is an entire web page along with its associated assets.

* The page returned has form elements.

* When you complete the form and submit it, the sever may find it invalid and
  subsequently send back an entire web page.

* The list of submissions only changes when the page is refreshed/changed.

---

# Demo App: Client-side

In a client-side web application:

* When you click the "New Submission" button, JavaScript executes and redraws
  the page to show a form. No HTTP request occurs.
* When you fill out the form and submit it, the input is validated in the
  browser using JavaScript (of course it also needs to be validated on the
  server-side in the event of misbehaving clients).
* If valid, an Ajax request is sent to the server.
* The list of submissions changes as new submissions are made (or thereabouts).

---

# Client-side Trade-offs

## Benefits

* UI is extremely responsive
* Less network traffic
* Live updates

## Weaknesses

* Client side code if much more complex
* First requests are significantly more expensive (lots more JavaScript to
send)

---

# Complex Client-side Code

Before this shift, the client mostly displayed static pages.

Now the client must:

* Understand the relationship between input events and corresponding DOM
  updates.
* Understand enough application logic to distinguish valid input from invalid
  input.
* Keep a persistent connection to the server and display updates as they come
  in.

---

# Application Design

> How should our application design adjust to this shift in complexity?

## Naïve Approach

Develop "JavaScript applications that end up as tangled piles of jQuery
selectors and callbacks, all trying frantically to keep data in sync between
the HTML UI, your JavaScript logic, and the database on your server."

UUUGHHHH!

---

# Client-side MVC

When something feels painful there is probably a better way to do it.

Enter client-side MVC frameworks.

---

# Client-side MVC Frameworks

## MVC: Model-View-Controller

* Rails is a server-side MVC.
* The presentation (view) of the data is separated from the data itself
  (model).
* Controllers exist to accept and coordinate updates to the models.
* Models encapsulate business logic and state.

There are many client-side frameworks that implement variations of the MVC
concept. We will introduce four:

* Backbone.js
* Angular
* Ember
* React

---

# Backbone.js

.fx: img-left

![Backbone](img/backbone.png)

* Developed by Jeremy Ashkenas (creator of CoffeeScript and Underscore.js)
* Most lightweight of the four libraries we will discuss
* Model-View-Router
* Router maps URL fragments to functions

## Websites using Backbone:

* Airbnb
* Hulu
* Groupon
* Pinterest
* LinkedIn

---

# Backbone Model-View

![Backbone Model View](img/backbone_model_view.png)

![Backbone Views](img/backbone_views.png)

---

# Backbone Model Sample

    !javascript
    var Sidebar = Backbone.Model.extend({
      promptColor: function() {
        var cssColor = prompt("Please enter a CSS color:");
        this.set({color: cssColor});
      }
    });
    window.sidebar = new Sidebar;
    sidebar.on('change:color', function(model, color) {
      $('#sidebar').css({background: color});
    });
    sidebar.set({color: 'white'});
    sidebar.promptColor();

---

# Backbone View Sample

    !javascript
    var DocumentRow = Backbone.View.extend({
      tagName: "li",
      className: "document-row",
      events: {
        "click .button.edit": "openEditDialog"
      },
      initialize: function() {
        this.listenTo(this.model, "change", this.render);
      },
      render: function() {
        this.$el.html(this.template(this.model.attributes));
        return this;
      }
    });

---

# Backbone Router Sample

    !javascript
    var Workspace = Backbone.Router.extend({

      routes: {
        "help":                 "help",    // #help
        "search/:query":        "search",  // #search/kiwis
        "search/:query/p:page": "search"   // #search/kiwis/p7
      },

      help: function() {
        ...
      },

      search: function(query, page) {
        ...
      }

    });

---

# Backbone Highlights

* Lightweight (1700 lines)
* Templating agnostic
* Doesn’t handle unbinding events
* Can lead to memory leaks
* For full-blown Single Page Apps, you might be better off with one of the
  larger frameworks

[http://backbonejs.org/](http://backbonejs.org/)

---

# Angular.js

.fx: img-left

![Angular Logo](img/angular.png)

* MVC framework supported and promoted by Google.
* Much larger and more complex than Backbone.
* Suitable for Single Page Applications.
* Emphasis on declarative style for building UI.
* Uses two-way data binding.

## Websites using Angular

* AWS console
* HBO
* VirginAmerica

---

# Angular Two-Way Data Binding

![Angular Two Way Data Binding](img/angular_two_way.png)

---

# Angular Data Binding Example

    !html
    <div ng-app ng-init="qty=1;cost=2">
      <div>
        Quantity: <input type="number" min="0" ng-model="qty">
      </div>
      <div>
        Costs: <input type="number" min="0" ng-model="cost">
      </div>
      <div><b>Total:</b> {{qty * cost | currency}}</div>
    </div>

---

# Angular Model Example

    !html
    <div ng-controller="Controller">
      Hello <input ng-model='name'> <hr/>
      <span ng-bind="name"></span> <br/>
    </div>

.

    !javascript
    angular.module('docsBindExample', [])
           .controller('Controller', ['$scope', function($scope) {
             $scope.name = 'Bryce';
           }]);

---

# Angular Highlights:

.fx: img-left

![Angular Logo](img/angular.png)

* Ambitious and large framework that really turns the page into an application
* Data binding provides a lot of magic
* A framework you adopt wholesale
* Declarative style retains HTML traditional nature

---

# Ember.js

.fx: img-left

![Ember Logo](img/ember.png)

* Created by prominent members of the Rails community
  (e.g., Yehuda Katz)

* Has much in common with Angular
    * All-in framework
    * Two way binding
    * Templating has similar flavor

---

# Ember Highlights

.fx: img-left

![Ember Logo](img/ember.png)

* Focus on convention over configuration
* Focus on standards compliance
* ES6 modules over custom modules
* ES6 polyfills in places

---

# React

.fx: img-left

![React](img/react.png)

* Developed at Facebook
* Observation: Event handling systems can be hard to reason about
    * Two-way binding helps take care of some of this automatically, but it can
      still be complex

> Why are server-side rendered systems simple to reason about?

---

# React Concept

.fx: img-left

![React](img/react.png)

If we could completely re-render the entire UI whenever anything changes, we
could develop systems that were very simple to reason about.

We can't re-render the entire UI because it would be too slow.

React allows you to build simple-to-reason-about UI code by making these
operations fast.

---

# React VirtualDOM

![React VirtualDOM](img/react_virtual_dom.png)

Instead of updating the DOM directly, keep track of modifications in a
"VirtualDOM", and only actually re-render what is needed.

---

# React: Simple Code

By giving the software engineer the ability to code as though he is
re-rendering everything each time, we get simple UI code:

    !javascript
    var HelloMessage = React.createClass({displayName: "HelloMessage",
      render: function() {
        return React.createElement("div", null, "Hello ", this.props.name);
      }
    });

    React.render(React.createElement(HelloMessage, {name: "John"}), mountNode);

---

# React Uses

.fx: img-left

![React](img/react.png)

Currently in production use at:

* Facebook
* Instagram
* Khan Academy

## React-native

* Build native mobile apps using these same techniques
* Not significant code-reuse from web to mobile, but tool-chain reuse.
* Available now for iOS, Android is in the works.

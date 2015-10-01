# HTML, CSS and Agile
.fx: title

__CS290B__

Dr. Bryce Boe

October 1, 2015

---

# Today's Agenda

* TODO
* HTTP Review
* Introduction to HTML
* Introduction to CSS
* Agile Software Development

---

# TO-DO

## Before Tuesday's Class:

* Complete [Ruby Code Academy](https://www.codecademy.com/tracks/ruby)
* Complete chapters 1 and 2 from Agile Web Development with Rails
* Complete chapters 1 and 2 in
[High Performance Browser Networking](http://chimera.labs.oreilly.com/books/1230000000545/ch01.html)
* Read chapters 9 through 11 in [High Performance Browser Networking](http://chimera.labs.oreilly.com/books/1230000000545/ch01.html)

---

# HTTP Components Review

![Components of HTTP request and response](img/http_components.png)

---

# Chrome Network Table

![Chrome Network Table](img/chrome_network_table.png)

---


# Review

> Why is the HOST header required in HTTP 1.1?

> What are the issues with using a TCP connection for each HTTP request?

> What is domain sharding?


---

# Introduction to HTML

---

# HyperText Markup Language

Plain text language that uses SGML syntax with a defined set of _tags_.

* Mark-up is provided by nesting text and other mark-up between `<open_tag>`
  and `</close_tag>`
* Tags are nestable
* Some tags have key-value attributes

Example:

    !html
    <h1>Header 1</h1>
    <h3>Header 3</h3>
    <p class="intro">A paragraph with some <em>emphasized text</em>.</p>

---

# HTML Document

HTML documents single root-element _should_ be the `<html>` tag. It's forest of
children are referred to as the _Document Object Model_ or __DOM__.

Technically are should be only two children of an `<html>` tag:

`<head>`: Encapsulates meta-data about the page including its title, and
   references to external resources (CSS, JavaScript)

`<body>`: Encapsulates everything to be displayed on the page

__Note__: With HTML5 (and many browsers' parsers for other variations of HTML)
these first-level tags can be omitted as they can be inferred based on the tag
being parsed.

---

# HTML5 Bootstrap Example

    !html
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Bootstrap 101 Template</title>

        <link href="css/bootstrap.min.css" rel="stylesheet">
      </head>

      <body>
        <h1>Hello, world!</h1>

        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
      </body>
    </html>

---

# Common HTML Tags

Different HTML tags should be used for different elements on the page. There
exist a handful of formatting and style tags, however, those should be avoided
in-favor of using CSS (cascading style sheets) -- we will discuss CSS later.

* __h1__ through __h6__: various header-level tags (h1 should be page title)
* __p__: paragraph text
* __ul__, __ol__: unordered and ordered list wrapper
* __li__: list item (nested within ul, or ol)
* __table__: begin a table
* __tr__: begin a table row within a table
* __td__: one entry in a table row
* __span__: An inline grouping mechanism
* __div__: A block-level grouping mechanism

---

# Anchor Tag

The most innovative part about HTML is the __HyperText__ part provided by the
anchor tag: `<a>`

Using an anchor tag one can link to another document (resource) anywhere on the
web.

    !html
    <a href="http://cs290.com">CS290</a>

---

# HTML Forms

An HTML form provides a convenient way to collect input from a web browser.

    !html
    <form action="/communities" method="post">
      <label for="cn">Name</label>
      <br>
      <input type="text" name="community" id="cn">
      <input type="submit" name="commit" value="Submit">
    </form>

## Notes

* `method` defaults to __GET__. Recall that __GET__ requests shouldn't
  have side-effects so __POST__ is more-often more appropriate.
* The default encoding is `application/x-www-form-urlencoded`

---

# Attributes `id` and `class`

HTML elements have two ubiquitous tags:

`id`: A unique identifier that makes it easy to find one element in the DOM

`class`: Multiple classes can be assigned to DOM elements, and the same class
can be applied to multiple DOM elements (many-to-many relationship).

    !html
    <span class="alert,loud" id="flash_message">Error.</span>

DOM IDs and classes are very useful for applying CSS, and adding JavaScript
callback hooks to elements on the page.

---

# Introduction to Cascading Style Sheets (CSS)

---

# The `<style>` tag

Inside the HTML `<head>` section we can use the `<style>` tag to add CSS
directly to the HTML.

Here we are styling all `h1` tags.

    !html
    <html>
      <head>
        <style>
          h1 {color: blue;}
        </style>
      </head>
      <body>
        <h1>Hello World</h1>
      </body>
    </html>

---

# Style via ID

DOM elements can be styled multiple ways.

Here we are styling all DOM elements with ID `header` (there should be at most
one per page).

IDs are prefixed with the `#` symbol in CSS.

    !html
    <html>
      <head>
        <style>
          #header {color: blue;}
        </style>
      </head>
      <body>
        <span id="header">Hello World</span>
      </body>
    </html>

---

# Style via Class

Here we are styling all DOM elements with class `alert`.

Classes are prefixed with the `.` symbol in CSS.

    !html
    <html>
      <head>
        <style>
          .alert {color: red;}
        </style>
      </head>
      <body>
        <span id="alert">Hello World</span>
      </body>
    </html>

---

# Inline Styles

We can use the `style` attribute on HTML tags to directly style
DOM elements.

    !html
    <html>
      <head>
        <style>
         /* nothing added here */
        </style>
      </head>
      <body>
        <span style="color: blue;">Hello World</span>
      </body>
    </html>

---

# Contradictory Styles

    !html
    <html>
      <head>
        <style>
          span {color: blue;}
          .a {color: yellow;}
          #b {color: green;}
        </style>
      </head>
      <body>
        <span class="a" id="b" style="color: red;">Hello World</span>
      </body>
      </html>

> What color is Hello World?

---

# Simplified Rule Precedence

In general more specific rules have higher precedence than less specific rules.

Precedence order (highest first):

* `!important` rules (e.g., `span {color: blue !important};`)
* Inline style
* ID
* Class
* HTML Tag

It gets more complicated, but understanding these rules will go a long way.

---

# External Style Sheets

Style definitions are most often provided through separate CSS files, rather
than `<style>` blocks.

    !html
    <html>
      <head>
        <link rel="stylesheet" href="style.css" type="text/css">
      </head>
      <body>
        <span>Hello World</span>
      </body>
      </html>


> Why might external styles be better than using the `<style>` tag, or inline
> styles?

---

# Visually Powerful

CSS is incredibly powerful. Changing a site's stylesheet can completely impact
how the site's users interact with the site.

This ends the brief overview of CSS.

To get started, it's definitely recommended to use a CSS framework like
Twitter's Bootstrap: [http://getbootstrap.com/](http://getbootstrap.com/)

---

# Bootstrap Alert Example

![Bootstrap Alert Example](img/bootstrap_alerts.png)

---

# Bootstrap Form Example

![Bootstrap Form Example](img/bootstrap_form.png)

---

# Agile Software Development

---

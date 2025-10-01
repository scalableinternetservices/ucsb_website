---
front_matter_title: ""
layout: default
navigation_weight: 2
permalink: /project1/
title: Project 1
navigable_page_name: project1
---

# Project 1: Static Web Page

Build, deploy, and load test a static web page hosted on GitHub Pages.

This project will ensure that students can deploy and load test a simple web
page prior to working with more complicated web applications.

Static web pages are fast to serve, and are relatively trivial to scale. Anyone
with access to a free GitHub account can deploy a static site that can
scale to thousands of users without requring any knowledge of how such scaling
is accomplished.

## Learning Outcomes

- Student can setup a git repository and use it for version control.
- Student can build and deploy a simple static web page.
- Student can measure average page load time.
- Student can measure server's rate limit.

## Project Submission

{% if site.project1_submission %}

<{{site.project1_submission}}>

{% else %}

- Submission link will be posted at start of quarter

{% endif %}

## Page Requirements

Your static page must:

- be hosted on [GitHub Pages](https://pages.github.com)
- be served via HTTPS
- be created by hand -- go nuts, but don't use a page generator, i.e., no more
  markup than necessary (ok to use language models to help with generation)
- contain 100% valid HTML5
- contain 100% valid CSS
- utilize an external style sheet to provide style changes (no inline styles,
  i.e., provided via `style` attributes)

You page must include:

- an external CSS file written by you and hosted on the same domain
- an index page including the following
  - a page title
  - a page heading
  - a paragraph of bio text telling me a bit about you
  - an image of you hosted on the same domain (helps me get to know your faces/names)
    If you object to putting your face on a public website, it is ok to skip this but please email me a photo of yourself so that I can create my own class roster with faces and add some other photo to your site.
  - a hyperlink to the GitHub repository containing the source code
  - A div with the id attribute set to "expert-topics" containing an unordered list with at least three 
  - a hyperlink to at least one page named /interest/<your_interest> Ex: /interests/airplanes
- a page for at least one of your interests accessible at /interest/<your_interest> Ex: /interests/airplanes
  - a page title
  - a page heading
  - a paragraph of text describing the content of this page
  - a table with at least 2 columns and at least 10 rows formatted as an FAQ about your topic of interest

### Verification Script

The `project1.py` script in
<https://github.com/scalableinternetservices/ucsb_website/tree/main/scripts>
can be used to automatically verify that your page meets the necessary
requirements.

Follow the directions in the README to clone the repository, install the python
dependencies, and run the verification script.

## Questions To Answer

- On average, how many requests can `ab` complete in 10 seconds with all the
  power of two concurrency levels between 1 and 256 (i.e., 1, 2, 4, 8, 16, 32,
  64, 128, 256)?
- Why are there diminishing returns at higher concurrency levels?
- What's the performance difference when requesting HTTP and HTTPS?
- How can GitHub respond so quickly?
- What is your site's "Total Blocking Time" (TBT) according to PageSpeed Insights?

## Required Tools

- [ab](https://httpd.apache.org/docs/2.4/programs/ab.html)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- git via [GitHub](https://help.github.com/en#dotcom)
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

## Other Resources

- [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)
- [W3C Markup Validation Service](https://validator.w3.org)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

---
front_matter_title: ""
layout: default
navigation_weight: 2
permalink: /project0/
title: Project 0
show_in_nav: true
---

# Project 0: Static Web Page

Build, deploy, and load test a static web page hosted on GitHub Pages.

This project will ensure that students can deploy and load test a simple web
page prior to working with more complicated web applications.

Static web pages are fast to serve, and are relatively trivial to scale. Anyone
with access to a free GitHub account can deploy a static web site that can
scale to thousands of users without requring any knowledge of how such scaling
is accomplished.

## Learning Outcomes

- Student can setup a git repository and use it for version control.
- Student can build and deploy a simple static web page.
- Student can measure average page load time.
- Student can measure server's rate limit.

## Project Submission

{% if site.project0_submission %}
<{{site.project0_submission}}>
{% else %}
- Submission link will be posted at start of quarter
{% endif %}

## Page Requirements

Your static webpage must:

- be hosted on [GitHub Pages](https://pages.github.com)
- be served via HTTPS
- be created by hand -- go nuts, but don't use a page generator, i.e., no more
  markup than necessary
- contain 100% valid HTML5
- contain 100% valid CSS
- utilize an external style sheet to provide style changes (no inline styles,
  i.e., provided via `style` attributes)

You webpage must include:

- a page title
- a page heading
- an image hosted on the same domain
- an external CSS file written by you and hosted on the same domain
- an unordered list with at least three items
- a table with at least 2 columns and at least 3 rows
- a hyperlink to the GitHub repository containing the source code

### Verification Script

The `project0.py` script in
<https://github.com/scalableinternetservices/ucsb_website/tree/main/scripts>
can be used to automatically verify that your webpage meets the necessary
requirements.

Follow the directions in the README to clone the repository, install the python
dependencies, and run the verification script.

## Questions To Answer

- On average, how many requests can `ab` complete in 10 seconds with all the
  power of two concurrency levels between 1 and 256 (i.e., 1, 2, 4, 8, 16, 32,
  64, 128, 256)?
- Why are there diminishing returns at higher concurrency levels?
- What's the performance difference when requesting HTTP and HTTPS?
- How can github respond so quickly?
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

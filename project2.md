---
layout: default
navigation_weight: 4
permalink: /project2/
title: Project 2
show_in_nav: false
---

# Project 2: AWS Lambda and JSON Web Tokens (JWT)

In this project you will write ruby code to provide a semi-trivial
HTTP API. Your code will be deployed using a single AWS Lambda function.

## Learning Outcomes

- Student has leveraged JWTs to provide authorization protection to HTTP
  endpoints.

- Student has utilized HTTP request methods, resources, headers, and bodies to
  differentiate between distinct HTTP requests.

- Student has implemented two endpoints to an HTTP API.

- Student can deploy code to AWS Lambda.

- Student has compared the performance of a static site to that of a dynamic site.

## Overview Video

<https://www.youtube.com/watch?v=Z1qmUASw58E>

## Project Submission

{% if site.project2_submission %}

<{{site.project2_submission}}>

{% else %}
- Submission link will be posted at start of quarter
{% endif %}

## API Specification

### GET /

This protected endpoint is used to simply reflect the content contained within
the `data` field of a valid JWT. It is a demonstration of how authorization can
be enforced on an endpoint.

- Requires a valid token from `POST /token` passed via the HTTP Header
  `Authorization` whose value is `Bearer <TOKEN>`.

- On success, returns a json document containing the contents of the `data`
  field from the provided token and responds with the status code `200`.

- Responds `401` if either the token is not yet valid, or if it is expired.

- Responds `403` if a proper `Authorization: Bearer <TOKEN>` header is not
  provided.

### POST /token

This endpoint is used to obtain the JWT necessary to request `/`. Normally such
an endpoint would be used to authenticate a user (e.g., verify a username and
password) before returning an authorization token. For simplicity we're skiping
the authentication step and will always return a token for a valid request.

- On success, returns a json document of the format `{"token": <GENERATED_JWT>}`
  with status code `201` where `<GENERATED_JWT>`:

  - uses a `HS256` signature (the symmetric key to use is in the environment
    variable `JWT_SECRET`)

  - contains exactly three fields

    - `data` which includes the request body from the HTTP requst

    - `exp` which is set to 5 seconds after the generation time

    - `nbf` which is set to 2 seconds after the generation time

- Responds `415` if the request content type is not `application/json`.

- Responds `422` if the body of the request is not actually json.

### Other Specifications

- All HTTP responses should have the content type `application/json`. You
  _shouldn't_ need to do anything to satisfy this requirement.

- Requests to any other resources must respond with status code `404`.

- Requests to `/` or `/token` which do not use the appropriate HTTP method must
  respond with status code `405`.

## Resources

### CS291 SSH Jump Box

The CS291 SSH jump box provides all the necessary configuration to deploy this
project to AWS. Using the `*.pem` file you were shared on Google Drive, ssh
into the jump box via:

    ssh -i <ACCOUNT_NAME>.pem <ACCOUNT_NAME>@ec2.cs291.com

Please note that if you have an underscore `_` in your UCSBNetId, then you'll
need to replace that with a hyphen `-`. For example, if your UCSBNetId is
`some_student`, you should have the file `some-student.pem`, and you will run
the command:

    ssh -i some-student.pem some-student@ec2.cs291.com

Once on the box you can clone the template repository:

    git clone https://github.com/scalableinternetservices/cs291a_project1_template.git

Then, run the file directly to ensure the example code works:

    cd cs291a_project1_template
    ruby function.rb

Deploy the function:

    ./deploy.py <ACCOUNT_NAME>

__Note__: Please do not do any load testing from this machine.

### Project Template

[https://github.com/scalableinternetservices/cs291a_project1_template](https://github.com/scalableinternetservices/cs291a_project1_template)

### Verification Script

Please use the following script to verify your web application:
<https://github.com/scalableinternetservices/ucsb_website/tree/main/scripts#project-1-verification-script>

## Questions To Answer

- On average, how many successful requests can `ab` complete to `/token` in 8
  seconds with various power-of-two concurrency levels between 1 and 256?

- Using data you've collected, describe how this service's performance compares
  to that of your static page from Project 0 (remeasure those results if
  necessary).

- What do you suspect accounts for the difference in performance between GitHub
  pages and your AWS Lambda web service?

## Required Tools

- [JSON Web Tokens](https://jwt.io/introduction/)

- [Ruby](https://www.ruby-lang.org/en/)

## Other Resources

- [AWS API
  Gateway](https://us-west-2.console.aws.amazon.com/apigateway/home?region=us-west-2#/apis)

- [AWS
  Lambda](https://us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2#/functions)

- [AWS CloudWatch
  Logs](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logs:)

- [ruby-jwt](https://github.com/jwt/ruby-jwt)

- [JSON Web Token RFC 7519](https://tools.ietf.org/html/rfc7519) (no need to
  really read through this all)

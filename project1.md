---
layout: default
navigation_weight: 3
permalink: /project1/
title: Project 1
---

# Project 1: AWS Lambda and JSON Web Tokens (JWT)

In this project you will write ruby code to provide a semi-trivial
HTTP API. Your code will be deployed using a single AWS Lambda function.

## Learning Outcomes:

- Student has leveraged JWTs to provide authorization protection to HTTP
  endpoints.

- Student has utilized HTTP request methods, resources, headers, and bodies to
  differentiate between distinct HTTP requests.

- Student has implemented two endpoints to an HTTP API.

- Student can deploy code to AWS Lambda.

- Student has compared the performance of a static website to that of a dynamic website.

## Due Date

Tuesday October 8, 10:59:59 AM PDT

## Project Submission

GOOGLE FORM LINK

## API Specification

### GET /

This protected endpoint is used to simply reflect the content contained within
the `data` field of a valid JWT. It is a demonstration of how authorization can
be enforced on an endpoint.

- Requires a valid token from `GET /token` passed via the HTTP Header
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

  - uses a HS256 signature (the symmetric key to use is in the environment
    variable `JWT_SECRET`)

  - contains exactly three fields

    - `data` which includes the request body from the HTTP requst

    - `exp` which is set to 5 seconds after the generation time

    - `nbf` which is set to 2 seconds after the generation time

- Responds `415` if the request content type is not `application/json`.

- Responds `422` if the body of the request is not actually json.


### Other Specifications

- All HTTP responses should have the content type `applicaiton/json`. You
  _shouldn't_ need to do anything to satisfy this requirement.

- Requests to any other resources must respond with status code `404`.

- Requests to `/` or `/token` which do not use the appropriate HTTP method must
  respond with status code `405`.


## Resources

### CS291 SSH Jump Box

TBD

### Project Template

[https://github.com/scalableinternetservices/cs291a_project1_template](https://github.com/scalableinternetservices/cs291a_project1_template)

### Verification Script

Please use the following script to verify your web application:
[https://github.com/scalableinternetservices/ucsb_website/tree/master/scripts#project-1-verification-script](https://github.com/scalableinternetservices/ucsb_website/tree/master/scripts#project-1-verification-script)

## Questions To Answer

TBD

## Required Tools:

- [JSON Web Tokens](https://jwt.io/introduction/)

- [Ruby](https://www.ruby-lang.org/en/)

## Other Resources:

- [AWS API
  Gateway](https://us-west-2.console.aws.amazon.com/apigateway/home?region=us-west-2#/apis)

- [AWS
  Lambda](https://us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2#/functions)

- [AWS CloudWatch
  Logs](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logs:)

- [ruby-jwt](https://github.com/jwt/ruby-jwt)

- [JSON Web Token RFC 7519](https://tools.ietf.org/html/rfc7519) (no need to
  really read through this all)

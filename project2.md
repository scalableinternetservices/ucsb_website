---
layout: default
navigation_weight: 4
permalink: /project2/
title: Project 2
---

# Project 2: Google's Cloud Run

In this project you will write a Sinatra application that is deployed to Google
Cloud Run. This service will provide a simple rest interface over a distributed
storage system, Google Cloud Storage (GCS), where your application can list,
get, and delete files.

Due to the fact that Google Cloud Run serves your application with many
different containers, we cannot simply store files on the local file system. 

## Learning Outcomes:

## Due Date

Tuesday October 15, 10:59:59 AM PDT

## API Specification

### GET /

- Reponds with `302` redirect to `/files/`.

### GET /files/

- Responds `200` outputting the sorted SHA256 of all files available in the system, on per line.

### POST /files/

### GET /files/{DIGEST}

- Respond `404` if there is no file corresponding to `DIGEST`.

- Respond `422` if `DIGEST` is not a valid SHA256 hex digest.

- On success, respond 200

  - `Content-Type` header should be set to that of the uploaded file.

  - The body should contain the contents of the file.

### DELETE /files/{DIGEST}

Delete the file represented by `DIGEST`.

- Respond `422` if `DIGEST` is not a valid SHA256 hex digest.

- Respond 200 in all other cases (recall that HTTP `DELETE` should be
  idempotent).


## Project Submission

GOOGLE FORM LINK

## Required Tools:

- [Docker](https://www.docker.com/products/docker-desktop)

- [Google Cloud Run](https://cloud.google.com/run/)

- [Google Cloud
  Storage](https://googleapis.dev/ruby/google-cloud-storage/latest/index.html)

- [Ruby](https://www.ruby-lang.org/en/)

- [Sinatra](http://sinatrarb.com/)

## Other Resources:

- [Google Cloud Tools](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version)

- [Google Cloud Run Quick
  Start](https://cloud.google.com/run/docs/quickstarts/build-and-deploy) (in
  case you want to look at doing this from scratch)

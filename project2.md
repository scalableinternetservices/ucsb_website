---
layout: default
navigation_weight: 4
permalink: /project2/
title: Project 2
---

# Project 2: Docker, Sinatra and Google's Cloud Run

In this project you will write a [Sinatra](http://sinatrarb.com/) application,
built it into a [Docker](https://www.docker.com/products/docker-desktop)
container, and deploy it [Google Cloud
Run](https://cloud.google.com/run/). This service will provide a simple rest
interface over a distributed storage system, Google Cloud Storage (GCS), where
your application can create, list, read, and delete files.

## Learning Outcomes:

- Student can perform create, read, and delete actions using Google Cloud
  Storage.

- Student has written a Sinatra web application with four API endpoints.

- Student has built a docker container.

- Student has deployed code to Google Cloud Run.

- Student has compared the performance of Google Cloud Run to that of AWS
  Lambda.

## Due Date

Tuesday October 15, 10:59:59 AM PDT

## Overview Video

[https://youtu.be/UOTows96LDA](https://youtu.be/UOTows96LDA)

## Project Submission

[https://forms.gle/jha4SDme75Put5KW6](https://forms.gle/jha4SDme75Put5KW6)

## HTTP API Specification

The following describes the HTTP API endpoints that you are to implement. The
template project provides only `GET /` that returns `Hello World`.

### GET /

This endpoint is simply used to redirect the client.

- Reponds with `302` redirect to `/files/`.

Example curl command:

```sh
curl -D- URL_BASE
```

Example HTTP response:

```http
HTTP/1.1 302 Found
location: URL_BASE/files/
```

### GET /files/

This endpoint is used to get a list of files available in the GCS bucket.

- Responds `200` with a JSON body containing a sorted list of valid SHA256
  digests in sorted order (lexicographically ascending).

Example curl command:

```sh
curl -D- URL_BASE/files/
```

Example HTTP response:

```http
HTTP/1.1 200 OK
content-type: application/json
Content-Length: 202

["02818fde32cc125a69bf5bdd2d1c1f615dee26984801ad3558cb7c71a54bc6ac","c36e18b713bf317e08e2afce764bf7e17457be9e22538efb39a9f0d036f7c6cc","fbcfc39ad67a080b85f914d3c37b10f6b814133fc1fcc321ac8c7e85cf42bc60"]
```

### POST /files/

This endpoint is used to upload a file to GCS.

- On success, respond `201` with a JSON body that encompasses the uploaded
  file's hex digest (see example below)

- Respond `409` if a file with the same SHA256 hex digest has already been
  uploaded.

- Respond `422` if:

  - there isn't a file provided as the `file` parameter

  - the provided file is more than `1MB` in size

Example curl command:

```sh
curl -D- URL_BASE/files/ -F 'file=@test.txt'
```

Example HTTP response:

```http
HTTP/1.1 201 Created
content-type: application/json
Content-Length: 79

{"uploaded":"3fd48de5c648bce27acaa6ddda51f35a0c69f07075ac472a4347c66502bb0d48"}
```

### GET /files/{DIGEST}

- On success, respond `200` and:

    - the `Content-Type` header should be set to that provided when the file
      was uploaded

    - the body should contain the contents of the file

- Respond `404` if there is no file corresponding to `DIGEST`.

- Respond `422` if `DIGEST` is not a valid SHA256 hex digest.

Example curl command:

```sh
curl -D- URL_BASE/files/3fd48de5c648bce27acaa6ddda51f35a0c69f07075ac472a4347c66502bb0d48
```

Example HTTP response:

```http
HTTP/1.1 200 OK
content-type: text/plain;charset=utf-8
content-disposition: attachment; filename="3fd48de5c648bce27acaa6ddda51f35a0c69f07075ac472a4347c66502bb0d48"
Content-Length: 10

Test File
```

### DELETE /files/{DIGEST}

Delete the file represented by `DIGEST`.

- Respond `422` if `DIGEST` is not a valid SHA256 hex digest.

- Respond 200 in all other cases (recall that HTTP `DELETE` should be
  idempotent).

Example curl command:

```sh
curl -D- -X DELETE URL_BASE/files/3fd48de5c648bce27acaa6ddda51f35a0c69f07075ac472a4347c66502bb0d48
```

Example HTTP response:

```HTTP
HTTP/1.1 200 OK
```

## Storage Requirements

Files are to be saved to the GCS bucket `cs291_project2` associated with the
project ID `cs291-f19`. The following ruby code provides an example for
obtaining a Bucket object:

```ruby
require 'google/cloud/storage'
storage = Google::Cloud::Storage.new(project_id: 'cs291-f19')
bucket = storage.bucket 'cs291_project2', skip_lookup: true
```

Uploaded files are to be saved into GCS using object names derived from the
SHA256 hex digest of the file's contents.

For example, the follow shows a file, `test.txt`, that has a SHA256 hex digest of
`3fd48de5c648bce27acaa6ddda51f35a0c69f07075ac472a4347c66502bb0d48`:

```sh
$ echo "Test File" > test.txt
$ sha256sum test.txt
3fd48de5c648bce27acaa6ddda51f35a0c69f07075ac472a4347c66502bb0d48  test.txt
```

The object name for the above file to store in GCS should be
`3f/d4/8de5c648bce27acaa6ddda51f35a0c69f07075ac472a4347c66502bb0d48`. In
particular we twice separate out two consecutive digits of the hex
digest. While this is an implementation specific detail that has no impact on
the external view of your API, it is important that this pattern is utilized.

## Resources

### Project Template

[https://github.com/scalableinternetservices/cs291a_project2_template](https://github.com/scalableinternetservices/cs291a_project2_template)

Please review the template project README for development and deployment instructions.

### Verification Script

Please use the following script to verify your web application:
[https://github.com/scalableinternetservices/ucsb_website/tree/master/scripts#project-2-verification-script](https://github.com/scalableinternetservices/ucsb_website/tree/master/scripts#project-2-verification-script)

## Required Tools:

- [Docker](https://www.docker.com/products/docker-desktop)

- [Google Cloud Run](https://cloud.google.com/run/)

- [Google Cloud
  Storage](https://googleapis.dev/ruby/google-cloud-storage/latest/index.html)

- [Ruby](https://www.ruby-lang.org/en/)

- [Sinatra](http://sinatrarb.com/)

## Other Resources:

- [Google Cloud
  Tools](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version)

- [Google Cloud Run Quick
  Start](https://cloud.google.com/run/docs/quickstarts/build-and-deploy) (in
  case you want to look at doing this from scratch)

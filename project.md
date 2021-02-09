---
layout: default
navigation_weight: 10
permalink: /project/
title: Primary Project
---

# Primary Project

## Objective

The goal of the project is to gain hands-on experience in building and
deploying a scalable web service on the Internet. Using the latest web
technologies while learning how to tackle the scalability and fault-tolerance
concerns. This is a "learn by doing" course: the course project will form the
primary focus of the course with the lectures and discussion of research papers
providing background material. Each project will be conducted in an agile team
where students will build their own scalable, redundant web site using
fundamental web technologies and the Ruby on Rails framework.

## Resources

Throughout the project, you might find it helpful to go through a ruby on rails tutorial. The Ruby on Rails Tutorial (see sidebar) is an amazing resource. Rail's own tutorial is quite good as well: [Getting Started with Rails](https://guides.rubyonrails.org/getting_started.html)

## Deliverables

### Report

Submit a report describing your project, and your data-driven approach to load testing. Consider answering the following questions:

- What bottlenecks did you encounter along the way, and how did you address them?
- What's the optimal $ cost per number of users your web service supports?
- What design or functionality tradeoffs did you have to make in order to support additional load?

#### Stellar Report Examples

- [Gaucho Book](/report_samples/gaucho_book.pdf)
- [Whatever Chat](/report_samples/whatever_chat.pdf)

### Video

Record a video presentation of your final project to share with the class. The video must be under 10 minutes in duration.

The video should emphasize your key results from your report.

## Project Sprint Schedule

All sprints end and begin with each week's lab session, save for the last
sprint which does not have an ending lab session.

At the end of each sprint you will:

- Ensure all your completed stories are integrated on your main branch.
- Deploy your project using Elastic Beanstalk.
- Demo your deployed version and share the newly created features.
- Share any new load testing results.


#### Sprint 1: Week 6

- Form your team.
  - Decide on a team name
  - One person on the team, message me on piazza with:
    - Your team name
    - The name, and GitHub username of all the team members
- Get access to your GitHub respository (I'll create that after the above)
- Get a new set of AWS credentials specific to your team.
- Deploy your initial rails code to Elastic Beanstalk.
- Complete `N` user stories, where `N` is the number of people on your team.
- Write a tsung load test encompassing your existing features.
  - Ensure that when it is run, there are no 4XX or 5XX level HTTP status
    codes.

#### Sprint 2: Week 7

#### Sprint 3: Week 8

#### Sprint 4: Week 9

#### Sprint 5: Week 10+

- Complete the [project report](#report)
- Create [project presentation video](#video)

---

## Creating a New Rails Application Using Docker

Assuming you have docker installed locally, follow the steps below to create a
new rails project using docker.

### Prepare the project directory


```sh
mkdir PROJECTNAME
cd PROJECTNAME
touch Dockerfile Gemfile Gemfile.lock docker-compose.yml
```

Copy the following contents into `Dockerfile`:

```docker
FROM ruby

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list \
  && apt-get update && apt-get install -y nodejs yarn --no-install-recommends \
  && gem install rails

WORKDIR /app

COPY Gemfile Gemfile.lock /app/
RUN bundle install

CMD ["/bin/bash"]
```

Copy the following contents into `docker-compose.yml`:

```yml
services:
  db:
    image: postgres
    volumes:
      - ./tmp/db:/var/lib/postgresql/data
  web:
    build: .
    command: bash -c "rm -f tmp/pids/server.pid && bundle exec rails s -p 3000 -b '0.0.0.0'"
    depends_on:
      - db
    ports:
      - "3000:3000"
    volumes:
      - .:/app:delegated
version: '3'
```

Initialize your git repository and make an initial commit:

```sh
git init
git add .
git commit -m "Prepare the project directory"
```

### Create the rails project

First build the `web` container image using `docker-compose`:

```sh
docker-compose build web
```

Then run `rails new` to create the initial rails project:

```sh
docker-compose run web rails new . --force --no-deps --database=postgresql
```

Add everything to git and make a new commit:

```sh
git add .
git commit -m "Run 'docker-compose run web rails new . --force --no-deps --database=postgresql'"
```

Finally, re-build the `web` container so that it now includes the project dependencies:

```sh
docker-compose build web
```

### Configure the project to talk to the database container

Add the following to lines to the `default` section of `config/database.yml`:

```yaml
  host: db
  username: postgres
```

Make a commit:

```sh
git add .
git commit -m "Configure the project to talk to the database container"
```

### Create the development and test databases

```sh
docker-compose run web rails db:create
```

### Ensure dependencies are up-to-date

Periodically run the following two commands to ensure your ruby and node
dependencies are up to date:

```sh
docker-compose run web bundle install
docker-compose run web yarn install
```

If your project has outstanding changes as shown via `git status`, consider making a
commit at this time.

### Start the development server

```sh
docker-compose up
```

At this point you _should_ be able to access the "Yay! You’re on Rails!" page
via [http://localhost:3000](http://localhost:3000).

---

## Deploying to Elastic Beanstalk

At this point you should have a Rails project that you can successfully run in
development locally using Docker. In the following steps we'll make the
necessary adjustments to configure the application for Amazon's Elastic
Beanstalk, and then deploy it.

### Configure the production database

Update the lines in the `production` section of `config.database.yml` to include:

```yaml
  database: <%= ENV['RDS_DB_NAME'] %>
  host: <%= ENV['RDS_HOSTNAME'] %>
  password: <%= ENV['RDS_PASSWORD'] %>
  port: <%= ENV['RDS_PORT'] %>
  username: <%= ENV['RDS_USERNAME'] %>
```

### Add ebextensions to install nodejs and yarn on each application server instance:

Create the directory and file

```sh
mkdir .ebextensions
touch .ebextensions/01_install_dependencies.config
```

Copy the following contents into `.ebextensions/01_install_dependencies.config`:

```
commands:
  install_nodejs:
    command: |
      curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
      yum -y install nodejs
  install_yarn:
    command: |
      sudo wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo
      yum -y install yarn
```

### Commit the changes

```sh
git add .
git commit -m "Prepare the application to deploy to Amazon's Elastic Beanstalk"
```

### Push changes to GitHub

If you haven't already, add GitHub as a remote:

```sh
git remote add origin git@github.com:scalableinternetservices/PROJECTNAME.git
```

If this is your first time pushing to GitHub, then run:

```sh
git push -u origin HEAD
```

Otherwise, you can simply run:

```sh
git push
```

### SSH to ec2.cs291.com and clone your repository

In order to most easily create an elastic beanstalk deployment, we need to SSH
into `ec2.cs291.com`. You should have received the file `TEAMNAME.pem` via your
UCSB Google Drive. Assuming that file is in your downloads folder run the
following:

```sh
ssh -i ~/Downloads/TEAMNAME.pem TEAMNAME@ec2.cs291.com
```

Once logged in, clone your repository using HTTPS (this will be a read-only
version of the project):

```sh
git clone https://github.com/scalableinternetservices/PROJECTNAME.git
```

### Configure Elastic Beanstalk

For each copy of your repository, you'll need to do the following only once:

```sh
cd PROJECTNAME
eb init --keyname $(whoami) \
  --platform "64bit Amazon Linux 2018.03 v2.11.0 running Ruby 2.6 (Puma)" \
  --region us-west-2 PROJECTNAME
```

### Create a deployment using the minimum necessary resources

```
eb create --envvars SECRET_KEY_BASE=BADSECRET \
  -db.engine postgres -db.i db.t3.micro -db.user u \
  -i t3.micro --single YOURNAME
```

Enter a database password at the prompt (twice) and then take a break as
creating a deployment will take about ten minutes (the database is slow to
create).

### Verify the deployment

Run `eb status` to see the state of your deployment. The output should look
something like the following:

```
Environment details for: YOURNAME
  Application name: PROJECTNAME
  Region: us-west-2
  Deployed Version: app-6360-191104_223036
  Environment ID: e-yetvigtxpz
  Platform: arn:aws:elasticbeanstalk:us-west-2::platform/Puma with Ruby 2.6 running on 64bit Amazon Linux/2.11.0
  Tier: WebServer-Standard-1.0
  CNAME: YOURNAME.yxhf954iam.us-west-2.elasticbeanstalk.com
  Updated: 2019-11-04 22:40:16.929000+00:00
  Status: Ready
  Health: Green
```

The two most important parts are that `Status` is `Ready`, and `Health` is
`Green`. If not consult the logs `eb logs`.

To test if the deployment is successful copy the CNAME, and paste it into your
browser:
[http://YOURNAME.yxhf954iam.us-west-2.elasticbeanstalk.com](http://YOURNAME.yxhf954iam.us-west-2.elasticbeanstalk.com)

If you get a page stating `The page you were looking for doesn't exist.`, that
likely means things are working, and you have yet to set up a `root_route` on
your site (the "Yay! You’re on Rails!" doesn't show up in `production` mode).

---

## Updating the application

After making changes and verifying they work with locally, push your changes to
GitHub, pull them on `ec2.cs291.com` and then update your deployment via:

```sh
eb deploy
```

__Note__: Only commited changes are pushed on deployment, so ensure `git
status` is clean. (You can run `eb deploy --staged` to include staged files,
but it's preferrable to deploy code that has been pushed to GitHub.

---

## Working with deployments

## Viewing Logs

To view the logs run:

```sh
eb logs | less -R
```

## SSH into an application server

```sh
eb ssh -i "ssh -i ~/$(whoami).pem"
```

### Cleaning Up

When you know you're done, clean up your deployment:


```
eb terminate
```

__Note__: Deployments will automatically be cleaned up ~110 minutes after their
last update.

---

## Project Ideas

Please select from one of the following project ideas. You are free to modify
them as you wish, and can even come up with another project idea, but the
complexity must remain the same.

Please note all the user stories start off with unauthenticated users. That's
because you want to deliver functionality first. Implementing authentication
first does not provide any value, if that authentication has no features behind
it. Complete a set of unauthenticated stories first, prior to introducing
authentication.

### A Social Network

Minimum necessary models:

- Post
- Comment (on Post)
- Profile
- Message (profile to profile)

Initial user stories:

0. As an unauthenticated user I can make a post so that I can share whatever
   cool things I want.

0. As an unauthenticated user I can view all the posts on the front page in
   descending order so that I can see what new things people are sharing.

0. As an unauthenticated user, I can comment on a post so that I can add
   updates to existing content.

0. As an authenticated user, my front page shows only posts made on my profile
   so that I can see content specific to me.

0. As as authenicated user, my posts and comments are attributable to me so
   that others know what I've shared.


### An Online Store

Minimum necessary models:

- Item
- Order
- Rating (user to item)
- User

Initial user stories:

0. As an unauthenticated user I can list my item on the store so that I can
   sell my products.

0. As an unauthenticated user I can purchase an item from the store so that I
   can obtain the things I desire.

0. As an unauthenticated user I can view all the purchase histories so that I
   can see what others have bought.

0. As an unauthenticated user, I can rate an item that has been purchased so
   that I can share my opinions of the item with others.

0. As an authenticated user, only I can see my own orders in my order history
   because I don't want others to see what I've purchased.


### An Event Sharing Service

Minimum necessary models:

- Event
- RSVP
- Comment
- User
- Invite

Initial user stories:


0. As an unauthenticated user, I can create an event so that I can share with
   others the details of the event I am hosting.

0. As an unauthenticated user, I can comment on an event to share my enthusiasm
   for said event.

0. As an authenticated user, I can RSVP yes/no to events that I do [not] indend
   to attend so that the host can better estimate how many people will show up.

0. As an authenticated user, I can see the list of events that I have
   previously attended so that I can recall my fond memories.

0. As an event host, I can proactively invite users to my event, so that I can help spread the word.



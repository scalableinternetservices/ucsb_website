---
front_matter_title: ""
layout: default
navigation_weight: 4
permalink: /project4/
title: Project 4
navigable_page_name: project4
---

# Project 4: Vertical and Horizontal Scaling of your Rails Backend

This project builds upon Project 3.  You should now have the backend of the help desk
application implementd in Ruby on Rails.  So far we have run the rails backend on localhost
only.  Now, we will deploy your web applications to AWS and charachterize the performance
of your applications by load testing the application in a few different configurations.


# Project Teams

This project and project 5 must be completed as part of a team.
Teams must be formed by Monday November 17th and be composed of 4 or 5 people.
Have one person on your team send me a message with the following details:
* Team Name
* Team Member Names


## Learning Outcomes

- Student can delpoy a Ruby on Rails application to [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
- Student can implement vertical scaling by modifying the AWS application instance size
- Student can implement vertical scaling by modifying the AWS database instance size
- Student can implement horizontal scaling by deploying multiple load balanced application instances
- Student can run write a load test using [Locust](https://locust.io/)
- Student can interpret the results of load tests

## Project Submission

{% if site.project4_submission %}

<{{site.project4_submission}}>

{% else %}

- Submission link will be posted at start of quarter

{% endif %}

## What's Included

- **AWS Credentials**: Credentials for accessing AWS services needed for deployment
- **Deployment Instructions**: Directions for deploying your rails appilcation to elastic beanstalk
- **Example Locustfile**: A basic example of a test file using Locust as a starting point
- **Scaled Infra Options to Test**: - A set of scaling configurations to run your load test against

## What you provide

- **Rails Application**: This should be a version of the rails backend from project 3
- **Locustfile**: A load test created using Locust

## What you will turn in

- **Locustfile**: The locustfile used for load testing your application
- **Load Testing Results**: A document that including the following sections
   - Load Test - Describes the methodology of your load test. This should include descriptions of user personas, tasks performed by each user, rationale for weighting of user personas and tasks.  Also included should be the methodology used for increasing the load during the test.  Ex: 1 new user arriving every second up to 500 users...
   - Load Test Results - For each deployment configuration, describe the configuration and the load testing results including plots and statistics.


## Scaling Configurations To Test

- Single Instance
   - 1 Application Server: Instance Type m7g.medium
   - 1 Database Server: Instance Type db.m5.large
- Vertical Scaling
   - 1 Application Server: Instance Type m7g.large
   - 1 Database Server: Instance Type db.m5.large
- Horizonal Scaling 1
    - 4 Application Servers: Instance Type m7g.medium
    - 1 Database Server: Instance Type db.m5.large
- Horizonal Scaling 2 w/ larger DB Instance
    - 4 Application Servers: Instance Type m7g.medium
    - 1 Database Server: Instance Type db.m5.xlarge

## Example Locustfile

```
"""
Locust load test for chat-backend-rails application.

User personas:
1. New user registering for the first time (1 in every 10 users)
2. Polling user that checks for updates every 5 seconds
3. Active user that uses existing usernames to create conversations, post messages, and browse
"""

import random
import threading
from datetime import datetime
from locust import HttpUser, task, between


# Configuration
MAX_USERS = 10000

class UserNameGenerator:
    PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def __init__(self, max_users=MAX_USERS, seed=None, prime_number=None):
        self.seed = seed or random.randint(0, max_users)
        self.prime_number = prime_number or random.choice(self.PRIME_NUMBERS)
        self.current_index = -1
        self.max_users = max_users
    
    def generate_username(self):
        self.current_index += 1
        return f"user_{(self.seed + self.current_index * self.prime_number) % self.max_users}"


class UserStore:
    def __init__(self):
        self.used_usernames = {}
        self.username_lock = threading.Lock()

    def get_random_user(self):
        with self.username_lock:
            random_username = random.choice(list(self.used_usernames.keys()))
            return self.used_usernames[random_username]

    def store_user(self, username, auth_token, user_id):
        with self.username_lock:
            self.used_usernames[username] = {
                "username": username,
                "auth_token": auth_token,
                "user_id": user_id
            }
            return self.used_usernames[username]


user_store = UserStore()
user_name_generator = UserNameGenerator(max_users=MAX_USERS)

class ChatBackend():
    """
    Base class for all user personas.
    Provides common authentication and API interaction methods.
    """        
    
    def login(self, username, password):
        """Login an existing user."""
        response = self.client.post(
            "/auth/login",
            json={"username": username, "password": password},
            name="/auth/login"
        )
        if response.status_code == 200:
            data = response.json()
            return user_store.store_user(username, data.get("token"), data.get("user", {}).get("id"))
        return None
        
    def register(self, username, password):
        """TODO"""

    def check_conversation_updates(self, user):
        """Check for conversation updates."""
        params = {"userId": user.get("user_id")}
        if self.last_check_time:
            params["since"] = self.last_check_time.isoformat()
        
        response = self.client.get(
            "/api/conversations/updates",
            params=params,
            headers=auth_headers(user.get("auth_token")),
            name="/api/conversations/updates"
        )
        
        return response.status_code == 200
    
    def check_message_updates(self, user):
        """TODO"""
    
    def check_expert_queue_updates(self, user):
        """TODO"""
    

class IdleUser(HttpUser, ChatBackend):
    """
    Persona: A user that logs in and is idle but their browser polls for updates.
    Checks for message updates, conversation updates, and expert queue updates every 5 seconds.
    """
    weight = 10
    wait_time = between(5, 5)  # Check every 5 seconds

    def on_start(self):
        """Called when a simulated user starts."""
        self.last_check_time = None
        username = user_name_generator.generate_username()
        password = username
        self.user = self.login(username, password) or self.register(username, password)
        if not self.user:
            raise Exception(f"Failed to login or register user {username}")

    @task
    def poll_for_updates(self):
        """Poll for all types of updates."""
        # Check conversation updates
        self.check_conversation_updates(self.user)
        
        # Check message updates
        self.check_message_updates(self.user)
        
        # Check expert queue updates
        self.check_expert_queue_updates(self.user)
        
        # Update last check time
        self.last_check_time = datetime.utcnow()

```

## Deploying to Elastic Beanstalk

At this point you should have a Rails project that you can successfully run in
development locally using Docker. In the following steps we'll make the
necessary adjustments to configure the application for Amazon's Elastic
Beanstalk, and then deploy it.

### Configure the production database

Update the lines in the `production` section of `config/database.yml` to include:

```yaml
database: <%= ENV['RDS_DB_NAME'] %>
host: <%= ENV['RDS_HOSTNAME'] %>
password: <%= ENV['RDS_PASSWORD'] %>
port: <%= ENV['RDS_PORT'] %>
username: <%= ENV['RDS_USERNAME'] %>
```

### Add ebextensions

Create the directory and file

```sh
mkdir .ebextensions
touch .ebextensions/01_environment_variables.config
```

Copy the following contents into `.ebextensions/01_environment_variables.config`:
```yaml
option_settings:
  aws:elasticbeanstalk:application:environment:
    # Make this the domain you want to server your application front end from.  This examples uses my github pages site
    # This isn't neccessary if you only want to run the frontend at localhost:5173
    FRONTEND_URL: "https://zwalker.github.io" 
    RAILS_ENV: "production"
    RAILS_SERVE_STATIC_FILES: "true"
```

Copy the following contents into `.ebextensions/healthcheck.config`:
```yaml
option_settings:
  aws:elasticbeanstalk:application:
    Application Healthcheck URL: /health
  aws:elasticbeanstalk:environment:process:default:
    HealthCheckPath: /health
```

### Configure the Profile

Inform elasticbeanstalk to use your chosen version of puma.

```sh
touch Procfile
```

Copy the following contents in `Procfile`:

```yaml
web: bundle exec puma -C /opt/elasticbeanstalk/config/private/pumaconf.rb
```

### Commit and push the changes

```sh
git add .
git commit -m "Prepare the application to deploy to Amazon's Elastic Beanstalk"
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

Once logged in, setup your ssh keys to access GitHub repo.
Generate the key pair:

```sh
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Then upload the key pair with read-only permissions to GitHub.

For more info see [Adding a new SSH key to your GitHub account
](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

After uploading your public key to GitHub, clone your repository using SSH
(this will be a read-only version of the project):

```sh
git clone git@github.com:scalableinternetservices/TEAMNAME.git
```

### Configure Elastic Beanstalk

For each copy of your repository, you'll need to do the following only once:

```sh
eb init --keyname $(whoami) --platform "64bit Amazon Linux 2023 v4.7.1 running Ruby 3.4" --region us-west-2 TEAMNAME
```

### Create a deployment using the minimum necessary resources

```sh
eb create --envvars SECRET_KEY_BASE=BADSECRET \
  -db.engine mysql -db.i db.t3.micro -db.user u \
  -i t3.micro --single YOURNAME
```

Enter a database password at the prompt (twice) and then take a break as
creating a deployment will take about ten minutes (the database is slow to
create).

### Verify the deployment

Run `eb status` to see the state of your deployment. The output should look
something like the following:

```yaml
Environment details for: YOURNAME
  Application name: TEAMNAME
  Region: us-west-2
  Deployed Version: app-f1ab-221021_194424258658
  Environment ID: e-7fm2cwv55t
  Platform: arn:aws:elasticbeanstalk:us-west-2::platform/Ruby 3.0 running on 64bit Amazon Linux 2/3.5.0
  Tier: WebServer-Standard-1.0
  CNAME: TEAMNAME.eba-6k3duymc.us-west-2.elasticbeanstalk.com
  Updated: 2022-10-21 19:45:40.487000+00:00
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

**Note**: Only commited changes are pushed on deployment, so ensure `git
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

```sh
eb terminate
```

**Note**: Deployments will automatically be cleaned up ~110 minutes after their
last update.
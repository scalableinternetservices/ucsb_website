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

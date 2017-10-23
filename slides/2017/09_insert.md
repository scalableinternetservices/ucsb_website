# Today's Agenda

* Deploying on Amazon Web Services (AWS)

---

# Deploying to AWS

Now that you all have a start to your rails application on Github, it is time
to learn how to deploy to AWS (Amazon Web Service).

Amazon provides a tool called Elastic Beanstalk that we will use to create
various deployments.

https://aws.amazon.com/elasticbeanstalk/

Note: I have verified that my demo app deploys. I need to make a few
cost-saving tweaks. Credentials should be usable again tomorrow.

---

# Working with AWS Guideliens

The AWS resources we will use are being donated by AppFolio. Please:

* __NEVER__ copy your AWS credentials into your code nor make them publicly
  available.

--

* Only deploy when you are ready to test something or demo.

* Terminate your deployment immediately when testing or the demo is done
  (billing is on 1-hour intervals from launch time).

--

* For demoing and deployment testing please only use a single `t2.micro`
  instance for the application server, and a `db.t2.micro` instance for the
  database, without a load balancer:

    ```
    eb create -db.i db.t2.micro -i t2.micro --single ...
    ```

---

# Working with AWS Guidelines

* For vertical scaling tests, always start with the smallest instance type and
  work your way up within the same deployment in order to minimize the time
  that larger instances are deployed for.
  http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.html

--

* For horizontal scaling tests, try to consistently use the smallest instance
  type that works for your application.
  http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.as.html

--

* Reset your database, and flush all caches between tests for consistency.

--

* Do not use any of the `micro` instances (app server or database) when
  performing scalability tests they have a CPU quota system that will affect
  results.

--

## When in doubt, please ask.

---

# AWS Instances and Data

Because instances should only be up for a limited amount of time it's important
to:

* Fetch any important data on the instances as soon as available (e.g., test
  results)

* Quickly load large amounts of testing data (test this process on smaller
  instances)

---

# Signing into AWS

Yesterday I sent a Piazza message to each team containing your team's private
ssh key (teamname.pem).

Use that to ssh into ec2.cs291.com

```bash
ssh -i teamname.pem teamname@ec2.cs291.com
```

Your AWS web console username and password be found in `~/teamname.txt`.

To login visit:
https://bboe-ucsb.signin.aws.amazon.com/console

## Oregon Region

Ensure that the __Oregon__ (us-west-2) region is selected in the upper right.

## Configuring your Application and Deploying

https://github.com/scalableinternetservices/demo_rails5_beanstalk

---

# By Next Wednesday

Demonstrate that you can successfully deploy your application to AWS by demoing
on AWS.

__Note__: All teams will be expected to demo on AWS for all following labs.

Launching a new deployment will take >10 minutes so kick it off prior to lab.

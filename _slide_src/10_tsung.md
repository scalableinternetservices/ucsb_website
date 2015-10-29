# Load Testing with Tsung
.fx: title

__CS290B__

Dr. Bryce Boe

October 29, 2015

---

# Peer Evaluation

Please discretely complete one of the peer evaluation forms and submit to me
when completed. Today's score is _only_ to show you where you stand relative to
your teammates.

After I have gone through the results, I will post a table of scores to piazza
using a one-way hash function of your perm number to the score only. I will
discuss with teams/individuals where potential grade-effecting discrepancies
exist.

We will do this again on November 17.

---

# Today's Agenda

* TODO
* Load Testing with Tsung

---

# TODO

* Keep making excellent progress on your project.
* Periodically ensure you can successfully deploy your project to AWS.
* Start thinking about what you want to test and how you will go about it.

## In Lab

* Deploy a Tsung instance on EC2
* Write an initial tsung xml file to load test a simple action on your
  application

---

# Load Testing with Tsung

After today you will know how to evaluate the scalability of a deployed web
application using Tsung.

Today will be interactive, so if you've brought your laptop feel free to
follow-along.

---

# Load Testing Motivation

Assume we are considering making a significant change to our web application.

We suspect that this change will improve our scalability.

> How can we confirm our suspicion?

---

# Load Testing

With load testing we can establish a baseline of expected performance of our
application.

We can then compare the results of previous load tests to those obtained after
making our changes.

> What should we observe?

* Response times
* Error rates
* Synthetic user success rate

---

# Modeling User Behavior

Ideally _real_ users would be used to compare an application's
performance.

Short of that, we want to create load-test flows that resemble
real trafic. There are a few things to consider:

* Ensuring flows contain a mixture of reads and writes
* Ensuring variance within the flows themselves (not all users have the same
  habits)
* The test framework should be able to utilize data returned from prior
requests (e.g., create a submission and make a comment on it)

> Why are these considerations important?

---

# Load Testing Tools

## High Performance Tools

* apachebench (ab)
* httperf
* Tsung

## Feature-rich Tools

* Funkload
* Tsung

## Others

* Bees with Machine Guns

Tsung is a good combination of the as it is extremely configurable and delivers
high performance. Today I will show you how to use it.

---

# Set Up

We ideally want one single-instance stack, and one load testing instance per
team.

* If you can, sit near your team.
* Deploy one `SinglePassenger` stack on a `m3.medium` instance.
    * [https://cs290b.s3.amazonaws.com/SinglePassenger.json](https://cs290b.s3.amazonaws.com/SinglePassenger.json)
* Deploy one `Tsung` stack on a `m3.medium` instance.
    * [https://cs290b.s3.amazonaws.com/Tsung.json](https://cs290b.s3.amazonaws.com/Tsung.json)


__Note__: `t2.micro` instances shouldn't be used for either end of
testing. These instances have a CPU quota, which when exceeded drastically
decreases the performance of the instance.

---

# Testing EC2 instances from EC2

We are going to launch the test instances in the same datacenter as our
stack. This decision provides us with:

* Lower cost: AWS charges for bandwidth outside of the datacenter)
* Predicitability: fewer moving parts between the test instance and the stack
* Less representative testing: none of our real users will be in the datacenter

The first two points are positive. The third point could be a concern, but
since we are essentially using these sort of tests for comparison between code
changes, we're less concerned with being completely representative.

---

# Launching a Tsung Stack

Use the normal proceedure:

* The stack name must be prefixed with your team name
* Use the `m3.medium` instance type unless you have a specific reason to use
  the larger types
* Select your team name

---

# Accessing the Tsung Instance

When the stack launch complets, the _Outputs_ tab will contain the SSH string
and a URL.

![Tsung Outputs tab](img/tsung_outputs.png)

At first accessing the URL will result in an error. It will be useful once
Tsung is running.

Use the SSH string to SSH into the Tsung instance.

---

# The Tsung Instance

The home directory of the tsung instance contains one file:

    !sh
    [ec2-user@ip-10-140-200-96 ~]$ ls
    simple.xml

`simple.xml` is a sample Tsung load-test configuration file that establishes 1
user each second to http://www.google.com.

Run this Tsung test via:

    tsung -f simple.xml -k start

One Tsung starts, visit the URL listed in the outputs.

---

# Tsung Server

While tsung runs (and continues to run after testing with the `-k` option) it
provides a simple web interface.

![Tsung Web Interface](img/tsung_interface.png)

---

# Tsung Interface

Out of the box, Tsung generates a report `/report.html`, and a handful of
graphs `/graphs.html`.

Additional graphs can be viewed directly at `/images/`.

The server, and web-based access to these files ceases to be accessible once
the Tsung process is stopped. Restarting Tsung only makes the graphs from the
current run available via the web interface.

---

# Fetching Tsung results

Aside from fetching files through the web interface. You may want to obtain all
of the Tsung results.

Assuming your SSH connect string is: `ssh -i demo.pem ec2-user@54.166.5.220`
then the following command will synchronize all the tsung result files (from
all runs) to your local machine:

    rsync -auve 'ssh -i demo.pem' ec2-user@54.166.5.220:.tsung/log/ .

Running that command a second time will only fetch any new files (assuming you
run it from the same path). rsync is awesome!

---

# The Tsung XML File

We will discuss some of the parts of the Tsung XML file. For a more complete
discussion please see Tsung's documentation:
[http://tsung.erlang-projects.org/user_manual/configuration.html](http://tsung.erlang-projects.org/user_manual/configuration.html)

# Tsung File Structure

    !xml
    <?xml version="1.0"?>
    <!DOCTYPE tsung SYSTEM "/usr/share/tsung/tsung-1.0.dtd">
    <tsung loglevel="notice" version="1.0">

      <clients>...</clients>
      <servers>...</servers>
      <load>...</load>
      <options>...</options>
      <sessions>...</sessions>
      ...

    </tsung>

---

# Tsung Clients Section

Reference: [http://tsung.erlang-projects.org/user_manual/conf-client-server.html](http://tsung.erlang-projects.org/user_manual/conf-client-server.html)

    !xml
    <clients>
      <client host="localhost" use_controller_vm="true" maxusers='30000'/>
    </clients>

The clients section specifies the clients to generate load from. While you can
use multiple machines as part of a single test, you probably won't need to.

---

# Tsung Servers Section

Reference: [http://tsung.erlang-projects.org/user_manual/conf-client-server.html](http://tsung.erlang-projects.org/user_manual/conf-client-server.html)

    !xml
    <servers>
      <server host="www.google.com" port="80" type="tcp"></server>
    </servers>

The servers section specifies where you intend to connect to. For your tests
you will always want to modify the `host` value to match your stack's
IP/domain.

---

# Tsung Load Section

Reference: [http://tsung.erlang-projects.org/user_manual/conf-load.html](http://tsung.erlang-projects.org/user_manual/conf-load.html)

    !xml
    <load>
      <arrivalphase phase="1" duration="60" unit="second">
        <users arrivalrate="2" unit="second"></users>
      </arrivalphase>
      <arrivalphase phase="2" duration="1" unit="minute">
        <users interarrival="2" unit="second"></users>
      </arrivalphase>
    </load>

Here we describe two phases.

The first phase lasts 60 seconds where 2 new users arrive (`arrivalrate`) each
second.

The second phase also lasts 60 seconds. Here 1 new user arrives
(`interarrival`) every two seconds.

---

# Tsung Options Section

Reference: [http://tsung.erlang-projects.org/user_manual/conf-options.html](http://tsung.erlang-projects.org/user_manual/conf-options.html)

    !xml
    <options>
      <!-- Set connection timeout to 2 seconds -->
      <option name="global_ack_timeout" value="2000"></option>

      <option type="ts_http" name="user_agent">
        <user_agent probability="100">Mozilla/5.0 ...</user_agent>
      </option>
    </options>

Unless you do something special with the user-agent in your web application,
you probably will not need to modify these options.

---

# Tsung Sessions Section

Reference: [http://tsung.erlang-projects.org/user_manual/conf-sessions.html](http://tsung.erlang-projects.org/user_manual/conf-sessions.html)

    !xml
    <sessions>
      <session name="http-example" probability="100" type="ts_http">
        <request>
          <http url='/' version='1.1' method='GET'></http>
        </request>
        <thinktime value="2" random="true"></thinktime>
        <request>
          <http url='/login' version='1.1' method='POST'
                contents="user=foo"></http>
        </request>
      </session>
    </sessions>

You can define multiple sessions and for each user one will be chosen according
to the probabilities.

---

# Load Testing Your Server

* Modify the `server` tag's `host` section to point to your web application
  URL/IP.
* Add a `request` tag for each resource fetched when you load your
  application's home page.
* Group requests to discrete _pages_ in `<transaction>` if you want statistics
  on the individual pages (don't include `<thinktime>` inside a transaction
  section.

---

# Dynamic Variables

---

# Tsung Output

* __request__: Response time for each request
* __page__: Response time for each set of requests (a page is a group of
  requests not separated by a thinktime)
* __connect__: The duration of the connection establishment
* __session__: The duration of a user's session

---

# Tsung HTTP Return Code

Inspect the HTTP return code section:

* 200 and 300 status codes are good
* 400 and 500 status codes can indicate problems:
    * Too many requests?
    * Server-side bugs?
    * Bug in testing code?

Ideally you shouldn't see any 400 and 500 status codes in your tests unless you
are certain they are due to exceeding the load on your web server's stack.

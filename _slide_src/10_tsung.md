# Load Testing with Tsung
.fx: title

__CS290B__

Dr. Bryce Boe

October 29, 2015

---

# Today's Agenda

* TODO
* Load Testing with Tsung

---

# TODO

* Keep making excellent progress on your project.
* Periodically ensure you can successfully deploy your project to AWS.
* Start thinking about what you want to test and how you will go about it.

---

# Load Testing with Tsung

After today you will know how to evaluate the scalability of a deployed web
application using Tsung.

Today can be interactive, so if you've brought your laptop feel free to
follow-along.

---

# Set Up

We ideally want one single-instance stack, and one load testing instance per
team.

* If you can, sit near your team.
* Deploy one `SinglePassenger` stack on a `m3.medium` instance.
* Deploy one `Tsung` stack on a `m3.medium` instance.

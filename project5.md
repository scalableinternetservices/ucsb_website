---
front_matter_title: ""
layout: default
navigation_weight: 5
permalink: /project5/
title: Project 5
navigable_page_name: project5
---

# Project 5: Enhanced Help Desk Application

Project 5 builds on all your projects so far.  This project will have 2 parts and will be due at the end of finals week.

## Part 1

In part 1 of this project you will work with your team to improve the chat application by adding:
* Auto assignment of newly created conversations to an expert
* Auto responsd to some questions based on the assinged expert's FAQ
* Provide a summary of a conversation in the conversation list view

These features will be implemented using calls to a Language Model (LLM).

At the completion of Part 1, your team should re-run the load tests run for project 4 and discuss the
results as a team.  At this point you should be comparing the results from before LLM features were
added with the new test results and preparing the first section of your final report.  In this section of the report you will describe:

* Initial load testing results from project 4 - (Before adding LLM features)
* Initial LLM feature implementation
    - Describe how the initial LLM features were implemented in step 1
* Load testing results after adding LLM features
    - Compare/contrast these results to those collected in project 4
    - If the results are different, discuss any hypothesis for the difference

## Part 2

Iteratively decide as a team on at least 3 changes to you application that you will make to improve the scalability of your application.  Before making the changes, document the reasoning for making these particular changes and make a hypothesis about how you expect the result of a subsequent load test will change from a previous test without the change in place.

Your team will then make changes to your application with the aim of improving the scalability of your application and re-run the load tests after each change.  For each change you should add a section to your team report describing:

* What was the change you decided to test
* What supporting evidence did you have to test this change
* What was the hypothesis about how this change would impact the load test results
* What was the observed impact on the load test results
* Discuss what was learned from running the load test and how it changes or confirms your original hypothesis

It is the goal to improve the scalability, but learning from something that does not improve the scalability can be equally valuable.  It is ok if your changes do not work, but you should have a good learning from those outcomes that can be discussed.

Each change should be tested in isolation so it can be determined what it's impact is in isolation.
This doesn't mean that you can't test the impact of multiple changes together.
For example: If you have BASELINE load test, CHANGE_A, CHANGE_B, and CHANGE_C, it would be ok to
* make CHANGE_A
* test CHANGE_A
* decide CHANGE_A was a success compared to the BASELINE test done before CHANGE_A
* merge CHANGE_A
* make CHANGE_B on top of the changes merged for CHANGE_A
* test CHANGE_B
* evaluate the results of testing CHANGE_A and CHANGE_B vs the test with just CHANGE_B
* ... continue on to merge CHANGE_B and test CHANGE_C in the same way

However, it would not be appropraite to evaluate a test of CHANGE_A, CHANGE_B togeher against the BASELINE test result in isolation.

It would also be ok to:
* make CHANGE_A
* load test CHANGE_A
* compare load test of CHANGE_A against the BASELINE
* without merging CHANGE_A, make CHANGE_B on a differen branch
* load test CHANGE_B
* compare load test of CHANGE_B against the BASELINE
* ...

If you choose to test the changes in isolation, you should do a final round of hypothesizing about what the impact will be of combining the succeful changes into a final branch will be and then do a final load test with those changes combined and discuss the results in comparision to the hypothesis and load tests done in isolation for the kept changes.


# Project Teams

This team must be comleted as part of a team.  You should be using the same team as you had for project 4.


## Learning Outcomes

- Student can reason about load test results
- Student can use evidence from results to create a hypotesis about a change to improve scalability
- Student can implement various scalability exeperiments
- Student can use load testing to evaluate the success of an experiment

## Project Submission

{% if site.project5_submission %}

<{{site.project5_submission}}>

{% else %}

- Submission link will be posted at start of quarter

{% endif %}


## What you will turn in

- **Github Repo**: Containing your final project including LLM feature additions and changes to improve scalability.
    - A merged Pull Request that implements the LLM features
    - A Pull Request (either merged or closed) for each scalability change discussed in the report
- **Report**: A report as described above.  Make sure to read the full project description to get an undersaning of what is expected in the report.


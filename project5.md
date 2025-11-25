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


## Instructions for using an LLM in your application


### Setup your project

Add the following gem to your Gemfile, then run `bundle install` 
```
gem "aws-sdk-bedrockruntime"
```

Add this file to you application in app/models/current.rb
```
class Current < ActiveSupport::CurrentAttributes
  attribute :might_be_locust_request
end
```

Add the following code to app/controllers/application_controller.rb
```
class ApplicationController < ActionController::API
  include ActionController::Cookies

  before_action :detect_locust_request

  private

  def detect_locust_request
    ua = request.user_agent.to_s

    if ua.include?("python-requests")
      Current.might_be_locust_request = true
    else
      Current.might_be_locust_request = false
    end
  end
end
```

Add the following code to app/services/bedrock_client.rb
```
# frozen_string_literal: true

require "aws-sdk-bedrockruntime"

class BedrockClient
  # Simple wrapper for calling an LLM on Amazon Bedrock (Converse API).
  #
  # Usage:
  #
  #   client = BedrockClient.new(
  #     model_id: "anthropic.claude-3-5-haiku-20241022-v1:0",
  #     region: "us-west-2"
  #   )
  #
  #   response = client.call(
  #     system_prompt: "You are a helpful assistant.",
  #     user_prompt:   "Explain eventual consistency in simple terms."
  #   )
  #
  #   puts response[:output_text]
  #
  def initialize(model_id:, region: ENV["AWS_REGION"] || "us-west-2")
    @model_id = model_id
    @client   = Aws::BedrockRuntime::Client.new(region: region)
  end

  # Calls the LLM with the given system and user prompts.
  #
  # Params:
  # - system_prompt: String
  # - user_prompt:   String
  # - max_tokens:    Integer (optional)
  # - temperature:   Float   (optional)
  #
  # Returns a Hash like:
  # {
  #   output_text: "model response...",
  #   raw_response: <Aws::BedrockRuntime::Types::ConverseResponse>
  # }
  #
  def call(system_prompt:, user_prompt:, max_tokens: 1024, temperature: 0.7)

    if should_fake_llm_call?
      sleep(rand(0.8..3.5)) # Simulate a delay
      return {
        output_text: "This is a fake response from the LLM.",
        raw_response: nil
      }
    end

    response = @client.converse(
      model_id: @model_id,
      messages: [
        {
          role: "user",
          content: [
            { text: user_prompt }
          ]
        }
      ],
      system: [
        {
          text: system_prompt
        }
      ],
      inference_config: {
        max_tokens: max_tokens,
        temperature: temperature
      }
    )

    output_text = extract_text_from_converse_response(response)

    {
      output_text: output_text,
      raw_response: response
    }
  rescue Aws::BedrockRuntime::Errors::ServiceError => e
    # You can customize error handling however you like.
    raise "Bedrock LLM call failed: #{e.message}"
  end

  private

  def should_fake_llm_call?
    !(ENV["ALLOW_BEDROCK_CALL"] == "true") or Current.might_be_locust_request
  end

  # Converse can return multiple content blocks; we’ll just join all text.
  def extract_text_from_converse_response(response)
    return "" unless response&.output&.message&.content

    response.output.message.content
            .select { |c| c.respond_to?(:text) && c.text }
            .map(&:text)
            .join("\n")
  end
end
```

### Instructions for local development

**KEEP THESE SECURE**

To use this this in local development, you will need to setup the AWS credentials in your localmachine.
To do this copy the ~/.aws/credentials file from the jump box to your localhost and put them in the same
location

**DO NOT CHECK THESE VALUSE INTO GITHUB**
```
scp project2backend@ec2.cs291.com:~/.aws/credentials ~/.aws/cs291_credentials
```

You will need to mount this as a volume in your docker compose to make the credentials work in local development

Add a new env var and volume to your web container in the docker compose to make the credentials available to the
app when running in your docker container
```
web:
    environment:
        - AWS_SHARED_CREDENTIALS_FILE=/app/.aws/cs291_credentials
    volumes:
        - ${HOME}/.aws:/app/.aws:ro   # 👈 mount your host AWS creds here
```


### Instructions for using the LLM when deployed to Elastic Beanstalk

I've added a few layers of protection to prevent calling the LLM in the load testing environment.

To be allowed access to call the LLM on bedrock from Elastic Beanstalk you will need to set the instance profile
to be used by your EC2 instances at the time you create your environment and set an ENV variable that will allow
the LLM to be called.  These protections are implmented in the BedrockClient shown above.

```
 eb create <env_name_goes_here> \
   --envvars "ALLOW_BEDROCK_CALL=true" \
   --profile eb-with-bedrock-ec2-profile \
   <Other parameters normally used>
```

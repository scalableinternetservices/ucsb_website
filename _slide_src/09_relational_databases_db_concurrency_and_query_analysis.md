# Relational Databases: Concurrency Control and Query Analysis
.fx: title

__CS290B__

Dr. Bryce Boe

October 22, 2015

---

# Today's Agenda

* TODO
* Server-side Caching in Rails Review
* A Stable Data Layer
* Database Concurrency Control
* Query Analysis

---

# TODO

## By end of lab

* As a team, launch your application on AWS
* Individually, confirm that you are able to SSH into your instance
* Shutdown your AWS stack(s)

---

# Rails Russian Doll Caching

    !erb
    <% cache(cache_key_for_submission_table) do %>

    <h3>Submissions</h3>
    <table class="table">
      <thead>
        <tr>...</tr>
      </thead>

      <tbody>
        <% @submissions.each do |submission| %>
          <% cache(...) do %> ... <% end %>
        <% end %>
      </tbody>
    </table>

    ...

    <% end %>

---

# Low-level Rails Caching

You can use the same built-in mechanisms to manually cache anything:

    !ruby
    class Product < ActiveRecord::Base
      def competing_price
        Rails.cache.fetch("#{cache_key}/competing_price",
                          expires_in: 12.hours) do
          Competitor::API.find_price(id)
        end
      end
    end

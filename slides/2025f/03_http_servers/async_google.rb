require 'async'
require 'async/http/client'
require 'async/http/endpoint'
require 'uri'

# Function to initiate concurrent requests
def fetch_concurrently(search_terms)
  endpoint = Async::HTTP::Endpoint.parse('https://www.google.com')
  client = Async::HTTP::Client.new(endpoint)

  Async do
    tasks = search_terms.map do |term|
      # Perform the request without waiting for results
      task = Async do |task|
        task.with_timeout(2) do
            puts "Searching for: #{term}"
            uri = URI::HTTPS.build(
              path: '/search',
              query: URI.encode_www_form(q: term)
            )
            response = client.get(uri.request_uri)
            response_body = response.save("/tmp/#{term}.html")
            puts "Response to search: #{term}"
            puts "Response status: #{response.status}"
        rescue Async::TimeoutError
	        puts "The request timed out"
        end
      end
    #   sleep(0.01)
      task 
    end

    tasks.each(&:wait) # Wait for all tasks to complete
  ensure
    client.close
  end
end

search_terms = [
  "kittens",
  "puppies",
  "mountain bikes",
  "santa barbara",
  "stocks"
]

# Initiate the searches
fetch_concurrently(search_terms)

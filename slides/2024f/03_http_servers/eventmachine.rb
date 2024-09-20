require 'eventmachine'
require 'em-http-request'

EM.run {
  test = EM::HttpRequest.new('https://cs291.com/').get
  test.errback { puts "cs291 is down! terminate?" }
  test.callback {
    search = EM::HttpRequest.new('http://google.com/search?q=em').get
    search.callback do 
        puts("got it")
        EM.stop { exit }
    end
    search.errback  { puts("error") }
  }
}
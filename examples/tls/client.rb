#!/usr/bin/env ruby
require 'openssl'
require 'socket'

MESSAGES = ["how are you?", "hello!", "my name is bryce", "QUIT"].freeze

def main
  server = TCPSocket.open("localhost", "1024")

  while line = server.gets
    puts line
    break if line == "SERVER CLOSING\n"
    server.puts(MESSAGES.sample)
  end
  server.close

  0 # Return code
end


def encrypted_main
  unencrypted_server = TCPSocket.open("localhost", "1024")
  encrypted_server = OpenSSL::SSL::SSLSocket.new(unencrypted_server)
  encrypted_server.sync_close = true
  encrypted_server.connect

  while line = encrypted_server.gets
    puts line
    break if line == "SERVER CLOSING\n"
    encrypted_server.puts(MESSAGES.sample)
  end
  encrypted_server.close

  0 # Return code
end

exit encrypted_main || 0 if __FILE__ == $PROGRAM_NAME

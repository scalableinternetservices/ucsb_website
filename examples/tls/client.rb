#!/usr/bin/env ruby
# frozen_string_literal: true

require 'openssl'
require 'socket'

MESSAGES = ['how are you?', 'hello!', 'my name is bryce', 'QUIT'].freeze

def add_encryption(socket)
  encrypted_server = OpenSSL::SSL::SSLSocket.new(socket)
  encrypted_server.sync_close = true
  encrypted_server.connect
  encrypted_server
end

def main
  server = TCPSocket.open('localhost', '1024')
  server = add_encryption(server)

  while (line = server.gets)
    puts line
    break if line == "SERVER CLOSING\n"

    server.puts(MESSAGES.sample)
  end
  server.close

  0 # Return code
end

exit main || 0 if __FILE__ == $PROGRAM_NAME

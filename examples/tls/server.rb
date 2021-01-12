#!/usr/bin/env ruby
require 'openssl'
require 'socket'

include Socket::Constants

def accept(socket)
  puts "Waiting for client..."
  client = socket.accept
  socket.close
  puts "Client connected"
  yield client
end


def tls_accept(socket)
  context = OpenSSL::SSL::SSLContext.new
  context.max_version = OpenSSL::SSL::TLS1_2_VERSION
  context.min_version = OpenSSL::SSL::TLS1_2_VERSION
  context.add_certificate(
    OpenSSL::X509::Certificate.new(File.open("certificate.crt")),
    OpenSSL::PKey::RSA.new(File.open("key.key"))
  ) 
  tls_socket = OpenSSL::SSL::SSLServer.new(socket, context)

  accept(tls_socket, &proc)
end


def main
  accept_socket = TCPServer.new('localhost', 1024)

  tls_accept(accept_socket) do |client|
    client.puts("CONNECTED")

    while line = client.gets
      if line == "QUIT\n"
        client.puts("GOODBYE!")
        break
      else
        client.write("ECHO: #{line}")
      end
    end

    client.puts("SERVER CLOSING\n")
    client.close    
  end

  0 # Return code
end

exit main || 0 if __FILE__ == $PROGRAM_NAME

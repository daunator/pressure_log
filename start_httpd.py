#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# taken from: http://stackoverflow.com/a/22533929/3282900

import SimpleHTTPServer
import SocketServer
import time
import thread

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_POST(self):
    if self.path.startswith('/kill_server'):
      print "Server is going down, run it again manually!"
      def kill_me_please(server):
        server.shutdown()
      thread.start_new_thread(kill_me_please, (httpd,))
      self.send_error(500)

class MyTCPServer(SocketServer.TCPServer):
  def server_bind(self):
    import socket
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind(self.server_address)

server_address = ('', 8000)
httpd = MyTCPServer(server_address, MyHandler)
try:
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()
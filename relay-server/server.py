import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import threading
from ws4py.client.tornadoclient import TornadoWebSocketClient

port = 9090

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("server working...")

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("ws opened")

    def on_message(self,message):
        self.write_message(message)

    def on_close(self):
        print("ws closed")

application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
])

if __name__ == "__main__":
  application.listen(port)
  print "server started at "+str(port)
  tornado.ioloop.IOLoop.instance().start()

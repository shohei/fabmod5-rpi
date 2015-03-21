import os
import commands
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("waiting for RML...") 

    def post(self):
        self.HandleRml()

    def HandleRml(self):
        rml = self.get_argument("rml")
	fout = open("output.rml","w")
	fout.write(rml)
        sendRmlCmd = "cat output.rml > /dev/ttyUSB0"
        print sendRmlCmd
        os.system(sendRmlCmd)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    port = 8080
    application.listen(port)
    print "listening on port",port
    tornado.ioloop.IOLoop.instance().start()



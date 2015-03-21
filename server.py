import os
import commands
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        self.HandleRml()

    def HandleRml(self):
        dispPortCmd = 'ls -l /dev/tty.* | sed -e "s/^.*dev/\/dev/g" | sed -n 1p'
        _,sport= commands.getstatusoutput(dispPortCmd)
        rml = "hoge.rml"
        sendRmlCmd = "cat " +rml+ " > "+sport
        print sendRmlCmd
        #os.system(sendRmlCmd)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    port = 8080
    application.listen(port)
    print "listening on port",port
    tornado.ioloop.IOLoop.instance().start()



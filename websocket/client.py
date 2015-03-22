#!/usr/bin/python
import websocket
import os

def on_open(ws):
    print "ws opened"

def on_close(ws):
    print "### closed ###"

def on_message(ws, message):
    print message
    fout = open("output.rml","w")
    fout.write(message)
    fout.close()
    HandleRml()

def on_error(ws, error):
    print error

def HandleRml():
    sendRmlCmd = "cat output.rml > /dev/ttyUSB0"
    print sendRmlCmd
    os.system(sendRmlCmd)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://133.242.160.150:9090/ws",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()


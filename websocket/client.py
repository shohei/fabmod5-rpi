#!/usr/bin/python
import websocket
import thread
import time


def on_message(ws, message):
    print message
    fout = open("output.rml","w")
    fout.write(message)
    fout.close()

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    print "ws opened"


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:9090/ws",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()


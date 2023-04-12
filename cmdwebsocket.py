import websocket
import rel
import json
import os
import data
from web import createAccount
#from Controlleur import Controlleur

# ctrl = Controlleur()
val = data.getGHState('data/GHState.json')
token=val["token"]
def on_message(ws, message):
    print("Received message : "+message)
    data = json.loads(message)
    cmds = json.dumps(data,indent=4)
    with open("new.json","w") as cmds_file:
        cmds_file.write(cmds)


def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):    
    print("Running...")

 

headers={'Content-Type':'application/json'}

if __name__ == "__main__":
    while os.stat('data/GHState.json').st_size == 0:
        print('The file is empty')
        createAccount()

    print('The file is not empty')
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://koraapi.alwaysdata.net/ws/serre/"+token+"/",
                                header=headers,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()

#!/usr/bin/env python


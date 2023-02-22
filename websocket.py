import websocket
import _thread
import time
import rel
import time
import json
import stomp
import stomper
import random

# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInByaW5jaXBhbF9uYW1lIjoiYWRtaW4iLCJpc3MiOiJBdGhlbmEiLCJ1c2VydHlwZSI6IkxPQ0FMIiwiYW9zX3ZlcnNpb24iOiJldXBocmF0ZXMtNS4xMS1zdGFibGUiLCJyZWdpb24iOiJlbi1VUyIsImV4cCI6MTczNDI4MDI3NywidXVpZCI6ImI4MzhjOGRkLWI4NmQtNGNkZS05ZTE4LTUxM2E1OTk4ODhhYyIsImlhdCI6MTU3NjYwMDI3NywiYXV0aG9yaXRpZXMiOiJST0xFX0NMVVNURVJfQURNSU4sUk9MRV9NVUxUSUNMVVNURVJfQURNSU4sUk9MRV9VU0VSX0FETUlOLFJPTEVfQ0xVU1RFUl9WSUVXRVIiLCJqdGkiOiI1NTU1ZjEwZC04NGQ5LTRkZGYtOThhNC1mZmI1OTM1ZTQwZWEifQ.LOMX6ppkcSBBS_UwW9Qo2ieWZAGrKqADQL6ZQuTi2oieYa_LzykNiGMWMYXY-uw40bixDcE-aVWyrIEZQbVsvA"
# headers = {"Authorization": "Bearer " + token}
def on_message(ws, message):
    # cmds = json.load(message)
    # print(cmds['temperature'])
    frame = stomper.Frame()
    unpacked_msg = stomper.Frame.unpack(frame, message)
    print("Received the message: " + str(frame.body))
    
    data = json.loads(frame.body)
    cmds = json.dumps(data,indent=4)
    with open("data/new.json","w") as cmds_file:
                cmds_file.write(cmds)
    

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):    
    print("Opened connection")
    ws.send("CONNECT\naccept-version:1.0,1.1,2.0\n\n\x00\n")
    client_id = str(random.randint(0, 1000))
    sub = stomper.subscribe("/topic/greeting",client_id, ack='auto')
    ws.send(sub)

    def run(*args):
        while True:
            try:
                with open("data/GHState.json",'r') as state_file:
                    state = json.load(state_file)
                data = json.dumps(state)
                time.sleep(3)
                ws.send(stomper.send("/app/greeting", data))
            except websockets.exceptions.ConnectionClosed:
                print("Client disconnected.  Do cleanup")
                break             
            print("thread terminating...")

    _thread.start_new_thread(run, ())

headers={'Content-Type':'application/json','Accept': 'text/plain'}
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8080/ws",
                                header=headers,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()

import json
import time
def updateval(val):
        stateJson = json.dumps(val,indent=4)  
        with open("data/identification.json","w") as state:
            state.write(stateJson)
class test2:
    def __init__(self):
       self.i=0
    def run(self):
        while True:
            x = """{"val":"""+str(self.i)+""" }"""
            data = json.loads(x)
            updateval(data)
            print(self.i)
            self.i=self.i+1
            time.sleep(3)

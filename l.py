# from Reader import Reader
import web
import time
# from Controlleur import Controlleur
from threading import Thread
import json
import subprocess


# ctrl = Controlleur()
# reader = Reader("","","",False,False)

class Backend(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.i=0
        self.start()
        

    def updateval(self,val):
        stateJson = json.dumps(val,indent=4)  
        with open("data/identification.json","w") as state:
            state.write(stateJson)
    def run(self):

        while True:
            x = """{"val":"""+str(self.i)+""" }"""
            data = json.loads(x)
            self.updateval(data)
            print(self.i)
            self.i=self.i+1
            time.sleep(3)
            # web.getCommands()
            
            # start = time.time()
            # while (time.time()-start) <= 30:
            #     ctrl.execute(reader)

            #     while (time.time()-start) <= 30:
            #         reader.getReadings()
            #         reader.updateGHState()
            #         print(start-time.time(),"sec")

            #     web.sendGHState()

class Frontend(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        subprocess.run("python3 test.py ",shell=True, check=True)


Backend()
Frontend()
while True:
    pass


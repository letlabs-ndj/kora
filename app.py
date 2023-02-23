from Reader import Reader
import web
import time
from Controlleur import Controlleur
from threading import Thread
import json
import data
import subprocess

reader = Reader()

class Backend(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.i=0
        self.start()
        
    def run(self):

        while True:
             #web.getCommands()
            
             start = time.time()
             while (time.time()-start) <= 10:
                 #ctrl.execute(Reader.reader)

                 while (time.time()-start) <= 10:
                     reader.getReadings()
                     print(time.time()-start,"sec")

                 web.sendGHState()

class Frontend(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        subprocess.run("python3 test.py --style material",shell=True, check=True)

if __name__ == "__main__":
    Backend()
    Frontend()
    while True:
        pass


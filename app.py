
import time
from threading import Thread
import subprocess



class Backend(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.i=0
        self.start()
        
    def run(self):
        subprocess.run("python3 Reader.py",shell=True, check=True)
        

class Frontend(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        subprocess.run("python3 gui.py --style material",shell=True, check=True)

class WebController(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        subprocess.run("python3 web.py",shell=True, check=True)

class ParamSender(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        subprocess.run("python3 web.py",shell=True, check=True)

class CommandGetter(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        subprocess.run("python3 cmdwebsocket.py",shell=True, check=True)

class TimeController(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        subprocess.run("python3 TimeController.py",shell=True, check=True)

if __name__ == "__main__":
    Backend()
    Frontend()
#    WebController()
#    TimeController()
    while True:
        pass


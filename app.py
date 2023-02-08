import web
import time
from Controlleur import Controlleur
from Reader import Reader

ctrl = Controlleur()
reader = Reader("","","",False,False)


while True:
    web.getCommands()
    start = time.time()
    while (time.time()-start) <= 30:
        ctrl.execute(reader)

        while (time.time()-start) <= 30:
            reader.getReadings()
            reader.updateGHState()
            print(start-time.time(),"sec")

        web.sendGHState()

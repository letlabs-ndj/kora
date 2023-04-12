import sys
import os
import datetime

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QTimer, QObject, Signal , Slot,QUrl
import json
from time import strftime, localtime
#from Controlleur import Controlleur
import data
import qrcode
from cmdwebsocket import token
import koraresource

#ctrl = Controlleur()

class Gui (QObject):
    def __init__(self):
        QObject.__init__(self)
        # QTimer - Run Timer
        self.timer = QTimer()    
        self.timer.timeout.connect(lambda: self.setTime())
        self.timer.start(1000)
        
        

     # Signal Set Data
    printTime = Signal(str)     

    def setToken(self):
        # Pass the current time to QML.
        curr_time = strftime("%H:%M:%S", localtime())
        engine.rootObjects()[0].setProperty('currTime', curr_time)

    def setControls(self):
        val = data.getGHState("data/GHState.json")
        sprinkler = val["arroseur"]
        ven = val["ventilateur"]
        tok = val["token"]
        engine.rootObjects()[0].setProperty("sprinkler",val["arroseur"])
        engine.rootObjects()[0].setProperty("ven",val["ventilateur"])
        engine.rootObjects()[0].setProperty("ampoule",val["ampoule"])
        engine.rootObjects()[0].setProperty("token",val["token"])

    def update_data(self):
        # Pass the current time to QML.
        val = data.getGHState('data/GHState.json')
        
        temp = val['temperature']
        hum = val['humiditeAir']
        lum = val['luminosite']

        engine.rootObjects()[0].setProperty('temp', temp)
        engine.rootObjects()[0].setProperty('hum', hum)
        engine.rootObjects()[0].setProperty('lum', lum)
        #engine.rootObjects()[0].setProperty('sprinkler', sprinkler)
        #engine.rootObjects()[0].setProperty('ven', ven)
       # engine.rootObjects()[0].setProperty('ampoule',ampoule)
        
    # @Slot(bool)
    # def ventilage(self,val):
    #     if val:
    #         print(val)
    #         ctrl.ventilage("true")
    #     else:
    #         print(val)
    #         ctrl.ventilage("false")
            
        

    # @Slot(bool)
    # def arrosage(self,val):
    #     if val:
    #         ctrl.arrosage("true")
    #         print(val)
    #     else:
    #         ctrl.arrosage("false")
    #         print(val)
        
    # @Slot(bool)
    # def eclairage(self,val):
    #     if val:
    #         ctrl.ajusterLuminosite("true")
    #         print(val)
    #     else:
    #         ctrl.ajusterLuminosite("false")
    #         print(val)

    @Slot(str,result=bool)
    def login(self,password):
        val = data.getGHState('data/identification.json')
        isValid = False

        if val['password'] == password:
            isValid=True

        return isValid

# Set Timer Function
    def setTime(self):
        now = datetime.datetime.now()
        formatDate = now.strftime("%H:%M:%S")
        print(formatDate)
        self.printTime.emit(formatDate)


if __name__== "__main__":
    # generating a QR code using the make() function  
    qr_img = qrcode.make(token)  
    # saving the image file  
    qr_img.save("assets/images/qr-img.jpg") 
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('qml/main.qml')

    gui = Gui()
    engine.rootObjects()[0].setProperty('gui', gui)
    engine.rootContext().setContextProperty("backend", gui)
    timer = QTimer()
    timer.setInterval(100)  # msecs 100 = 1/10th sec
    timer.timeout.connect(gui.update_data)
    timer.start()

    sys.exit(app.exec_())

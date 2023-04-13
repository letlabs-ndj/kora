import sys
import os
import datetime

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QTimer, QObject, Signal , Slot,QUrl
import json
from time import strftime, localtime
# from Controlleur import Controlleur
import data
import qrcode
import koraresource

# ctrl = Controlleur()
def openDialog():
    dis = distantConn()
    engine.rootContext().setContextProperty("backend", dis)
    dis.conn("yes")           

class distantConn(QObject):
    def __init__(self):
        QObject.__init__(self)
        # QTimer - Run Timer

    distantUser = Signal(str)

    def conn(self,email):
        self.distantUser.emit(email)


class Gui (QObject):
    def __init__(self):
        QObject.__init__(self)
        # QTimer - Run Timer
        self.timer = QTimer()    
        self.timer.timeout.connect(lambda: self.setTime())
        self.timer.start(1000)
        
        

     # Signal Set Data
    printTime = Signal(str) 
    distConn=Signal(str)      

    # def update_time(self):
    #     # Pass the current time to QML.
    #     curr_time = strftime("%H:%M:%S", localtime())
    #     engine.rootObjects()[0].setProperty('currTime', curr_time)

    def setControls(self):
        val = data.getGHState("data/GHState.json")
        sprinkler = val['arroseur']
        ven = val['ventilateur']
        ampoule = val["lumiere"]
        token = val["token"]
        engine.rootObjects()[0].setProperty("sprinkler",sprinkler)
        engine.rootObjects()[0].setProperty("ven",ven)
        engine.rootObjects()[0].setProperty("ampoule",ampoule)
        engine.rootObjects()[0].setProperty("token",token)

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
        
    @Slot(bool)
    def ventilage(self,val):
        if val:
            print(val)
            ctrl.ventilage("true")
        else:
            print(val)
            ctrl.ventilage("false")
            
        

    @Slot(bool)
    def arrosage(self,val):
        if val:
            ctrl.arrosage("true")
            print(val)
        else:
            ctrl.arrosage("false")
            print(val)
        
    @Slot(bool)
    def eclairage(self,val):
        if val:
            ctrl.ajusterLuminosite("true")
            print(val)
        else:
            ctrl.ajusterLuminosite("false")
            print(val)

    @Slot(str,result=bool)
    def login(self,password):
        val = data.getGHState('data/identification.json')
        isValid = False

        if val['password'] == password:
            isValid=True

        return isValid

    # @Slot(str,result=str)
    # def isSerreConnection(self,req):
    #     val = json.loads(req)
    #     text = data["text"]
    #     type=""
    #     if text["type"]=="Serre Connection":
    #         type="SC"
    #     elif text["type"]=="Change Propertie":
    #         type="CP"
    #     else:
    #         type="none"

    #     print(type)
    #     return type

    @Slot(result=str)
    def getUserEmail(self):
        val = data.getGHState("data/serreConnect.json")
        return val["email"]

    @Slot(result=str)
    def getUserTok(self):
        val = data.getGHState("data/serreConnect.json")
        return val["token"]
    
# Set Timer Function
    def setTime(self):
        now = datetime.datetime.now()
        formatDate = now.strftime("%H:%M:%S")
        print(formatDate)
        self.printTime.emit(formatDate)


if __name__== "__main__":
    # generating a QR code using the make() function  
    qr_img = qrcode.make("letlabs")  
    # saving the image file  
    qr_img.save("assets/images/qr-img.jpg") 
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('qml/main.qml')

    gui = Gui()
    dis = distantConn()
    engine.rootObjects()[0].setProperty('gui', gui)
    engine.rootContext().setContextProperty("backend", gui)
    
    timer = QTimer()
    timer.setInterval(100)  # msecs 100 = 1/10th sec
    timer.timeout.connect(gui.update_data)
    gui.setControls()
    timer.start()

    sys.exit(app.exec_())
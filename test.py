import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QTimer, QObject, Signal , Slot
import json
from time import strftime, localtime

class Gui (QObject):
    def __init__(self):
        super().__init__()

    def update_time(self):
        # Pass the current time to QML.
        with open("data/GHState.json", "r") as cmds_file:
                    val = json.load(cmds_file)
        temp = val['temperature']
        hum = val['air_humidity']
        lum = val['light_intensity']
        sprinkler = val['sprinkler_status']
        ven = val['fan_status']
        engine.rootObjects()[0].setProperty('temp', temp)
        engine.rootObjects()[0].setProperty('hum', hum)
        engine.rootObjects()[0].setProperty('lum', lum)
        engine.rootObjects()[0].setProperty('sprinkler', sprinkler)
        engine.rootObjects()[0].setProperty('ven', ven)

    @Slot(str)
    def text(self,txt):
        print(txt)

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

gui = Gui()
engine.rootObjects()[0].setProperty('gui', gui)
timer = QTimer()
timer.setInterval(100)  # msecs 100 = 1/10th sec
timer.timeout.connect(gui.update_time)
timer.start()

sys.exit(app.exec_())
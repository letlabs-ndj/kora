import schedule
import time
import datetime
from Controlleur import Controlleur

ctrl = Controlleur()

def arrosage_18h():
    ctrl.arrosage("true")

def stop_arrosage_18h():
    ctrl.arrosage("true")

def eclairage_18h():
    ctrl.ajusterLuminosite(100)

def stop_eclairage_18h():
    ctrl.ajusterLuminosite(0)

def job():
    schedule.every().day.at('18:00').do(arrosage_18h)
    schedule.every().day.at('18:05').do(stop_arrosage_18h)
    schedule.every().day.at('04:41').do(eclairage_18h)
    schedule.every().day.at('6:00').do(stop_eclairage_18h)


job()

while True:
    schedule.run_pending()
    time.sleep(1)

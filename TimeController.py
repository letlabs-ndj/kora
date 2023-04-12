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
    ctrl.ajusterLuminosite("true")

def stop_eclairage_18h():
    ctrl.ajusterLuminosite("true")

def job():
    schedule.every().day.at('09:25').do(arrosage_18h)
    schedule.every().day.at('09:30').do(stop_arrosage_18h)
    schedule.every().day.at('09:25').do(eclairage_18h)
    schedule.every().day.at('09:35').do(stop_eclairage_18h)


job()

while True:
    schedule.run_pending()
    time.sleep(1)

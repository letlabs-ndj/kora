import time
import board
import adafruit_dht
import psutil
import os
import datetime
import RPi.GPIO as GPIO
import json

class Reader(object):
    instance = None
    temperature = ""
    air_humidity = ""
    light_intensity =""
    sprinkler_status = False
    fan_status = False

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls,*args,**kargs)
        return cls.instance

    def __init__(self,temp,hum,light,spr,fan):
        self.temperature = temp
        self.air_humidity = hum
        self.light_intensity = light
        self.sprinkler_status = spr
        self.fan_status = fan    

    def getReadings(self):
        for proc in psutil.process_iter():
            if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
                
                proc.kill()
        sensor = adafruit_dht.DHT11(board.D23)
        while True:
            try:
                GetDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                light_intensity = self.readLdr()
                temperature = sensor.temperature
                air_humidity = sensor.humidity
                print("Temperature: {}*C   Humidity: {}% ".format(temperature, air_humidity))
                print("luminosite: {}".format(light_intensity)) 

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                sensor.exit()
                raise error
            time.sleep(2.0)
    
    def readLdr (self):
        count = 0
        time.sleep(.1)
        while (GPIO.input(ldr) == 0):
            count += 1

        return count



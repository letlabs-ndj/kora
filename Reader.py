import adafruit_dht
import time
import board
import psutil
import os
import datetime
import RPi.GPIO as GPIO
import json

ldr = 7
dhtSensor = adafruit_dht.DHT11(board.D23)
GPIO.setup(ldr, GPIO.OUT)
GPIO.output(ldr, GPIO.LOW)

class Reader(object):
    instance = None    

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
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
        
        try:
            GetDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.light_intensity = self.readLdr()
            self.temperature = dhtSensor.temperature
            self.air_humidity = dhtSensor.humidity
            print("Temperature: {}*C   Humidity: {}% ".format(self.temperature, self.air_humidity))
            print("luminosite: {}".format(self.light_intensity)) 

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
        except Exception as error:
            dhtSensor.exit()
            raise error
        time.sleep(2.0)
    
    def updateGHState(self):
        stateJson = json.dumps(self.instance.__dict__,indent=4)  
        with open("data/GHState.json","w") as state:
            state.write(stateJson)
    
    def readLdr (self):
        count = 0
        time.sleep(.1)
        GPIO.setup(ldr, GPIO.IN)
        while (GPIO.input(ldr) == GPIO.LOW):
            count += 1

        return count

    

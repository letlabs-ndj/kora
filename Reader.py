import time
import board
import adafruit_dht
import psutil
import os
import datetime
import RPi.GPIO as GPIO
import json
import data
import busio
import adafruit_ccs811
from board import *

#i2c = board.I2C()   # uses board.SCL and board.SDA
#ccs =  adafruit_ccs811.CCS811(i2c)


ldr = 12 #UV led pin

#We define which pin to use and the type of sensor we which to read (In our case we want to read a
#DHT11 sensor
dhtSensor = adafruit_dht.DHT11(board.D23,use_pulseio=False)


#The Reader will be resposible for reading all sensors at a time and store their values
#It will also store the state of our different equipements
class Reader(object):
    instance = None    

#We should only have one Reader object in the whole system. So we ensure ourselves that
#there will be only one instance of the Reader class in the system.
    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self):
        return None
        #self.temperature = '0'
        #self.air_humidity = '0'
        #self.light_intensity = '0'
        #self.CO2Level = '0'
        #self.sprinkler_status = True
        #self.fan_status = False    


#The function that will permit the Reader object to read all the sensors
    def getReadings(self):
        self.readTempAndHum() 
        self.readLdr()
        
        val = data.getGHState()
        
        val['temperature']=data.sensorData["temperature"]
        val['air_humidity']=data.sensorData["air_humidity"]
        val['light_intensity']=data.sensorData["light_intensity"]
        
        data.updateGHState(val)
        
        time.sleep(1.0)
    


    
#The function for reading light intensity from light dependent resistor
    def readLdr (self):
        count = 0
        GPIO.setup(ldr, GPIO.OUT)
        GPIO.output(ldr, GPIO.LOW)
        time.sleep(1)
        GPIO.setup(ldr, GPIO.IN)
        while (GPIO.input(ldr) == GPIO.LOW):
            count += 1
        
        data.sensorData["light_intensity"] = int(100-(count/5000)*100)
        print("luminosite: {}".format(data.sensorData["light_intensity"]))
        

#The function for reading the temperature and air humidity
    def readTempAndHum (self):
    #We make sure there is no libgpiod process running. If it is the case we kill it
        for proc in psutil.process_iter():
            if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
                
                proc.kill()        
        
        try:
            data.sensorData["temperature"] = int(dhtSensor.temperature) #we get the temperature
            data.sensorData["air_humidity"] = int(dhtSensor.humidity)  #we get the air humidity
            print("Temperature: {}*C   Humidity: {}% ".format(data.sensorData["temperature"], data.sensorData["air_humidity"]))
            

        except RuntimeError as error:
            print(error.args[0])
        except Exception as error:
            dhtSensor.exit()
            raise error
    
    
    def readAirQuality(self):
        data.sensorData["CO2Level"] = int(ccs.eco2)
        print("CO2: ", ccs.eco2, " TVOC:", ccs.tvoc)
        

import time
import board
import adafruit_dht
import psutil
import os
import glob
import datetime
import RPi.GPIO as GPIO
import json
import data
import data
import busio
import serial
import adafruit_ccs811
from board import *

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'


#tempsensor = W1ThermSensor()

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
        

#The function that will permit the Reader object to read all the sensors
    def getReadings(self):
        self.readHum() 
        self.readLdr()
        #self.readTemp()
        
        val = data.getGHState("data/GHState.json")
        
        val['temperature']=data.sensorData["temperature"]
        val['humiditeAir']=data.sensorData["humiditeAir"]
        val['luminosite']=data.sensorData["luminosite"]
        
        
        data.updateGHState(val)
        
        time.sleep(1.0)
    


    
#The function for reading light intensity from light dependent resistor
    def readLdr (self):        
        ser = serial.Serial('/dev/ttyACM0', 9600)

        # Lire la donnée reçue depuis la Raspberry Pi
        val = ser.readline().decode().strip()
        print(val)
        data.sensorData["luminosite"]=val

        print("luminosite: {}".format(data.sensorData["luminosite"]))
        
        # Fermer la connexion série
        ser.close()

#The function for reading the temperature and air humidity
    def readHum (self):
    #We make sure there is no libgpiod process running. If it is the case we kill it
        for proc in psutil.process_iter():
            if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
                
                proc.kill()        
        
        try:            
            data.sensorData["humiditeAir"] = int(dhtSensor.humidity)  #we get the air humidity

            print("Humidity: {}% ".format(data.sensorData["humiditeAir"]))
            

        except RuntimeError as error:
            print(error.args[0])
        except Exception as error:
            dhtSensor.exit()
            raise error
    
    def readTemp (self):
        temp_c = sensor.get_temperature()
        
        def read_temp_raw():
            f = open(device_file, 'r')
            lines = f.readlines()
            f.close()
            return lines

        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            data.sensorData["temperature"] = int(temp_c) #we get the temperature
            # temp_f = temp_c * 9.0 / 5.0 + 32.0
            
    
    def readAirQuality(self):
        data.sensorData["CO2Level"] = int(ccs.eco2)
        print("CO2: ", ccs.eco2, " TVOC:", ccs.tvoc)
        


if __name__ == "__main__":
    reader = Reader()
    while True:
        reader.getReadings()
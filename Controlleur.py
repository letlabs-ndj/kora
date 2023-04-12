import json
#import Reader
import enum
import RPi.GPIO as GPIO
import data

GPIO.setwarnings(False)

pinArro = 8
pinVen = 18
pinAmp =25

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinArro, GPIO.OUT)
GPIO.setup(pinVen, GPIO.OUT)
GPIO.setup(pinAmp, GPIO.OUT)

class Commands(enum.Enum):
 Arrosage = 'humiditeSol'
 Ventilation = 'humiditeAir'
 Eclairage = 'luminosite'


class Controlleur(object):
    instance = None

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def execute(self,param,val):
            if param == Commands.Arrosage.value:
                print('arro')
                self.arrosage(val)                

            elif param == Commands.Ventilation.value:
                print('ven')
                self.ventilage(val)                

            else:
                self.ajusterLuminosite(val)
                print('lum')
    

    def arrosage(self,val):
         a=False
         if val=="true":
             a=True
             print('arrosage actif')
             
         else:
             a=False
             print('arrosage non-actif')
         
         GPIO.output(pinArro, a)
         val = data.getGHState("data/GHState.json")
        
         val['arroseur']=a
   
         data.updateGHState(val)

                                                                                                                                                                                                                                                                                                                                 
    def ventilage(self,val):
         a=False
         if val=="true":
             a=True
             print('ventilo actif')
         else:
             a=False
             print('ventilo non-actif')
             

         GPIO.output(pinVen, a)
         
         val = data.getGHState("data/GHState.json")
        
         val['ventilateur']=a
   
         data.updateGHState(val)

      
    def ajusterLuminosite(self,val):
         a=False
         if val=="true":
             a=True
             print('ampoule actif')
             print(a)
         else:
             a=False
             print("ampoule non-actif")
	
         GPIO.output(pinAmp,a)
         val=data.getGHState("data/GHState.json")
         val['luminosite']=a
         data.updateGHState(val)
               
        

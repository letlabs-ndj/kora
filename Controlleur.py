import json
import Reader
import enum
import RPi.GPIO as GPIO
from gpiozero import PWMLED
import data

GPIO.setwarnings(False)

pinArro = 7
pinVen = 18
light = PWMLED(17)

GPIO.setup(pinArro, GPIO.OUT)
GPIO.setup(pinVen, GPIO.OUT)


class Commands(enum.Enum):
 Arrosage = 'Arrosage'
 Ventilation = 'Ventilation'
 Eclairage = 'Eclairage'


class Controlleur(object):
    instance = None

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def execute(self,reader):
        with open("data/commands.json", "r") as cmds_file:
            cmds = json.load(cmds_file)

        for cmd in cmds:
            if cmd['type'] == Commands.Arrosage.value:
                print('arro')
                self.arrosage(reader,cmd['val'])
                

            elif cmd['type'] == Commands.Ventilation.value:
                print('ven')
                self.ventilage(reader,cmd['val'])
                

            else:
                self.ajusterLuminosite(int(cmd['val']))
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
         val = data.getGHState()
        
         val['sprinkler_status']=a
   
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
         
         val = data.getGHState()
        
         val['fan_status']=a
   
         data.updateGHState(val)

      
    def ajusterLuminosite(self,val):
         light.value = val/100
         print(val)
               
        

import json
import enum

class Commands(enum.Enum):
    Arrosage = 'Arrosage'
    Ventilation = 'Ventilation'
    Eclairage = 'Eclairage'


class Controlleur(object):
    instance = None

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls,*args,**kargs)
        return cls.instance

    def execute(self,commande,reader):
        cmd = json.loads(commande)
        if cmd['type'] == Commands.Arrosage:
            self.actionner(17,cmd['val'])            
        elif cmd['type'] == Commands.Ventilation:
            self.actionner(18,cmd['val'])
        else:
            self.ajusterLuminosite(cmd['val'])

        self.updateReader(cmd['type'],reader,cmd['val'])

    

    def actionner(self,sensorPin,val):
        if val:
            print('arrosage actif')
            GPIO.output(sensorPin, val)
        else:
            print('arrosage non-actif')
            GPIO.output(sensorPin, val)

      
    def ajusterLuminosite(self,val):
        light.value = val/100
               
    
    def updateReader(self,param,reader,val):
        if param == Commands.Arrosage:
            reader.sprinkler_status = val
        elif param == Commands.Ventilation:
            reader.fan_status = val
        
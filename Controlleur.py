# import json
# import enum
# import RPi.GPIO as GPIO
# from gpiozero import LED

# GPIO.setwarnings(False)
# pinArro = 7
# pinVen = 18
# light = PMWLED(17)

# GPIO.setup(pinArro, GPIO.OUT)
# GPIO.setup(pinVen, GPIO.OUT)


# class Commands(enum.Enum):
#     Arrosage = 'Arrosage'
#     Ventilation = 'Ventilation'
#     Eclairage = 'Eclairage'


class Controlleur(object):
    instance = None

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def execute(self):
        with open("data/commands.json", "r") as cmds_file:
            cmds = json.load(cmds_file)

        for cmd in cmds:
            if cmd['type'] == Commands.Arrosage.value:
                print('arro')
                self.arrosage(cmd['val'])
                

            elif cmd['type'] == Commands.Ventilation.value:
                print('ven')
                self.ventilage(cmd['val'])
                

            else:
                self.ajusterLuminosite(cmd['val'])
                print('lum')



    

    def arrosage(self,val):        
        # if val:
        #     print('arrosage actif')
        # else:
        #     print('arrosage non-actif')

        # self.sprinkler_status = val
        # GPIO.output(pinArro, val)
        print('arose')


    def ventilage(self,val):        
        # if val:
        #     print('ventilo actif')
        # else:
        #     print('ventilo non-actif')

        # self.fan_status = val
        # GPIO.output(pinVen, val)
        print('vent')

      
    def ajusterLuminosite(self,val):
        # light.value = val/100
        print('light')
               
        

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
            cls.instance = object.__new__(cls)
        return cls.instance

    def execute(self):
        with open("commands.json", "r") as cmds_file:
            cmds = json.load(cmds_file)

        for cmd in cmds:
            if cmd['type'] == Commands.Arrosage.value:
                self.actionner()
                

            elif cmd['type'] == Commands.Ventilation.value:
                self.actionner()
                

            else:
                self.ajusterLuminosite()


    def actionner(self):        
        print('arro/ven')

      
    def ajusterLuminosite(self):
        print('lum')
               



ctrl = Controlleur()
ctrl.execute()
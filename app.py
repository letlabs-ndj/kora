import json

class Reader(object):
    instance = None
    temperature = ""
    air_humidity = ""
    light_intensity =""
    sprinkler_status = False
    fan_status = False

    def __init__(self,temp,hum,light,spr,fan):
        self.temperature = temp
        self.air_humidity = hum
        self.light_intensity = light
        self.sprinkler_status = spr
        self.fan_status = fan

def updateGHState(state):
        stateJson = json.dumps(state.__dict__,indent=4)  
        with open("GHState.json","w") as state:
            state.write(stateJson)

read = Reader("yes","no","2",False,False)
updateGHState(read)
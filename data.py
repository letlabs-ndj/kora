import json

sensorData ={
    "temperature": 0,
    "humiditeAir": 0,
    "luminosite": 0,
}

def getGHState(file):
    with open(file, encoding="utf-8") as f:
        data = json.load(f)
    return data
    
#The function that will permit the Reader object to save the actual state of the greenhouse
#in a json file
def updateGHState(data):
#we convert the object into a json
    stateJson = json.dumps(data,indent=4)
#we then write the json into a json file
    with open("data/GHState.json","w") as state:
        state.write(stateJson)

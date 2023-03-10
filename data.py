import json

sensorData ={
    "temperature": 0,
    "air_humidity": 0,
    "light_intensity": 0,
    "CO2Level": "0"
}

def getGHState():
    with open('data/GHState.json', 'r+') as f:
        data = json.load(f)
    return data
    
#The function that will permit the Reader object to save the actual state of the greenhouse
#in a json file
def updateGHState(data):
#we convert the reader instance into a json
    stateJson = json.dumps(data,indent=4)
#we then write the json into a json file
    with open("data/GHState.json","w") as state:
        state.write(stateJson)

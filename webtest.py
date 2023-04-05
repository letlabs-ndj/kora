import requests
import json
import time
#from Controlleur import Controlleur

def getCommands():
    try:
        response = requests.get('https://koraapi.alwaysdata.net/api/v1/com/',
        headers={'Accept': 'application/json'})
        print(f"Status Code: {response.status_code}, Content: {response.json()}")

        cmds = json.dumps(response.json(),indent=4)
        with open("data/commands.json","w") as cmds_file:
                cmds_file.write(cmds)
    except:
        pass
    

def sendGHState():
    try:
        with open("data/GHState.json",'r') as state_file:
                state = json.load(state_file)

        data = json.dumps(state)
        headers={'Content-Type':'application/json','Accept': 'text/plain'}

        response = requests.put('https://koraapi.alwaysdata.net/api/v1/serre/',data=data,headers=headers)
    except:
        pass
    
if __name__ == "__main__":
   getCommands()
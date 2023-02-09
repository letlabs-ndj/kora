import requests
import json

def getCommands():
    try:
        response = requests.get('http://localhost:8080/get',
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

        response = requests.post('http://localhost:8080/post',data=data,headers=headers)
    except:
        pass
    

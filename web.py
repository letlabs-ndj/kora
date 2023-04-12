import websocket
import rel
from time import sleep
import json
import requests
import os
import data


def createAccount():
    try:
        with open("account.json",'r') as state_file:
            state = json.load(state_file)

        dictionary = {}
        data = json.dumps(dictionary)
        response = requests.post('https://koraapi.alwaysdata.net/api/v1/serre/',data=data,
        headers={'Content-Type':'application/json'},timeout=5)
        print(f"Status Code: {response.status_code}, Content: {response.json()}")

        id = json.dumps(response.json(),indent=4)
        with open("data/info.json","w") as id_file:
                id_file.write(id)

    except requests.ConnectionError:
        print("Pas de connexion internet disponible")

def sendGHState():
    try:
        val = data.getGHState('data/GHState.json')
        id=str(val["id"])
        with open("data/GHState.json",'r') as state_file:
            state = json.load(state_file)

        params = json.dumps(state)
        response = requests.put("https://koraapi.alwaysdata.net/apps/serre/"+id+"/",data=params,
        headers={'Content-Type':'application/json'},timeout=5)
        print(response.json())

        params = json.dumps(response.json(),indent=4)
        with open("data/GHState.json","w") as param_file:
                param_file.write(params)

    except requests.ConnectionError:
        print("Pas de connexion internet disponible")



headers={'Content-Type':'application/json'}

if __name__ == "__main__":
    while os.stat('data/GHState.json').st_size == 0:
        print('The file is empty')
        createAccount()

    while True:
        sendGHState()
        sleep(2)
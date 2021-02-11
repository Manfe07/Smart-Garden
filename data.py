import json
import paho.mqtt.client as mqtt


with open("config.json") as json_data_file:
    config = json.load(json_data_file)

def getSensors():
    json_data={
        "Gemüsebeet":{
            "temp": 24.5,
            "hum": 71.4,
            "soil": 40
        },
        "Tomaten": {
            "temp": 32.5,
            "hum": 34.4,
            "soil": 60
        },
        "Zimmer": {
            "temp": 22.5,
            "hum": 71.4,
            "soil": 40
        },
        "Zuchtkasten": {
            "temp": 28.3,
            "hum": 60.3,
            "soil": 70
        }
    }
    return json_data

def getPumps():
    pumps = {
        "Tomaten":{
            "state": True,
            "level": 20,
            "percent": 70
        },
        "Gemüsebeet":{
            "state": False,
            "level": None,
            "percent": None,
        }
    }
    return pumps
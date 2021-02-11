import json
from influxdb import InfluxDBClient

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

if(config['influxdb']['user'] == ""):
    db_client = InfluxDBClient(host=config['influxdb']['hostname'], port=config['influxdb']['port'])
else:
    db_client = InfluxDBClient(host=config['influxdb']['hostname'], port=config['influxdb']['port'], username=config['influxdb']['user'], password=config['influxdb']['passwd'])

db_client.create_database(config['influxdb']['database'])
db_client.switch_database(config['influxdb']['database'])

def handleMessage(topic, payload):
    data = json.loads(payload)
    print(data)
    if topic == config['mqtt']['baseTopic'] + "/sensor":
        if data['type'] == "clima":
            place = data['data']['place']
            temp = data['data']['temp']
            humidity = data['data']['hum']
            pressure = data['data']['press']

            json_body =[{
                "measurement": "clima",
                "tags": {
                    "place": place,
                },
                "fields":{
                    "temp": temp,
                    "humidity": humidity,
                    "pressure": pressure
                }
            }]
            return  db_client.write_points(json_body)


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
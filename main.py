from flask import Flask, render_template
import data, json
from flask_mqtt import Mqtt

with open("config.json") as json_data_file:
    config = json.load(json_data_file)


app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = config['mqtt']['hostname']
app.config['MQTT_BROKER_PORT'] = config['mqtt']['port']
app.config['MQTT_USERNAME'] = config['mqtt']['user']
app.config['MQTT_PASSWORD'] = config['mqtt']['passwd']
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe(f"{config['mqtt']['baseTopic']}/#")

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data.handleMessage(message.topic, message.payload.decode())

@app.route("/")
def index():
    return render_template('index.html', clima=data.getSensors(), pumps=data.getPumps())

@app.route("/setting")
def setting():
    return render_template('setting.html')


if __name__ == "__main__":
    app.run()

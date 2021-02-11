from flask import Flask, render_template
import data, json
import paho.mqtt.client as mqtt

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(f"{config['mqtt']['baseTopic']}/#")

def on_message(client, userdata, msg):
    payload = str(msg.payload.decode("utf-8"))
    topic = msg.topic
    print(topic + " " + payload)
    data.handleMessage(topic, payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=config['mqtt']['user'], password=config['mqtt']['passwd'])
client.connect(host=config['mqtt']['hostname'], port=config['mqtt']['port'])
client.loop_start()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', clima=data.getSensors(), pumps=data.getPumps())

@app.route("/setting")
def setting():
    return render_template('setting.html')


if __name__ == "__main__":
    app.run(debug=True)

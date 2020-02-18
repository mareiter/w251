import paho.mqtt.client as mqtt
from datetime import datetime

MQTT_HOST = "mosquitto"
MQTT_PORT = 1883
MQTT_TOPIC = "hw3_faceDet"
QOS = 1

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Local MQTT Broker")

def on_message(client, userdata, msg):
    print("Image Received")
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = "/mnt/mareiter-hw03/face_" + now + '.png'
    imagefile = open(path, 'wb')
    imagefile.write(msg.payload)
    imagefile.close()
    print("Image Saved")

mqttclient = mqtt.Client("Image Processor")
mqttclient.on_connect = on_connect
mqttclient.on_message = on_message

mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)
mqttclient.subscribe(MQTT_TOPIC, qos=QOS)

mqttclient.loop_forever()

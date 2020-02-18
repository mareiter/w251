import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST = "mosquitto"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "hw3"
QOS = 1

CLOUD_MQTT_HOST = "159.8.200.186"
CLOUD_MQTT_PORT = 1883
CLOUD_MQTT_TOPIC = "hw3_faceDet"

def on_connect_local(client, userdata, flags, rc):
    print("Connected to Jetson")
    client.subscribe(LOCAL_MQTT_TOPIC)

def on_connect_cloud(client, userdata, flags, rc):
    print("Connected to Cloud")
    client.subscribe(CLOUD_MQTT_TOPIC)

def on_message(client, userdata, msg):
    print("Image Received")
    print("Publishing to Cloud")
    cloudmqttclient.publish(CLOUD_MQTT_TOPIC, payload=msg.payload, qos=QOS, retain=False)

localmqttclient = mqtt.Client("Forwarder")
localmqttclient.on_connect = on_connect_local
localmqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
localmqttclient.on_message = on_message

cloudmqttclient = mqtt.Client("Forwarder")
cloudmqttclient.on_connect = on_connect_cloud
cloudmqttclient.connect(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)

localmqttclient.loop_forever()
cloudmqttclient.loop_forever()

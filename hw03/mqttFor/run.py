import paho.mqtt.client as mqtt

#MQTT_HOST = "172.20.0.2"
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "hw3"

CLOUD_MQTT_HOST = "159.8.200.186"
CLOUD_MQTT_PORT = 1883
CLOUD_MQTT_TOPIC = "hw3_faceDet"

def on_connect(client, userdata, flags, rc):
    print("Connected to jetson")

def on_connect_cloud(client, userdata, flags, rc):
    print("Connected to cloud")

def on_message(client, userdata, msg):
    print("on message received")
    cloudmqttclient.publish(CLOUD_MQTT_TOPIC,payload=msg.payload,qos=2,retain=False)

cloudmqttclient = mqtt.Client()
cloudmqttclient.connect(CLOUD_MQTT_HOST,CLOUD_MQTT_PORT,60)
cloudmqttclient.on_connect = on_connect_cloud 

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect 
mqttclient.on_message = on_message 

mqttclient.connect(MQTT_HOST,MQTT_PORT,60)
mqttclient.subscribe(MQTT_TOPIC, qos=2)

mqttclient.loop_forever()  # Start networking daemon


#### Previous ####
'''
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST = "mosquitto"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "hw3_faceDet"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    print("message received!")	
    # if we wanted to re-publish this message, something like this should work
    # msg = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
'''

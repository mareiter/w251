import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt

MQTT_HOST = "mosquitto"
MQTT_PORT = 1883
MQTT_TOPIC = "hw3"
QOS = 1 

def on_connect(client, userdata, flags, rc):
    print("Connected to Local Broker")

mqttclient = mqtt.Client("Face Detector")
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        face = frame[y:y+h, x:x+w]
        print("Face Detected ", face.shape, face.dtype)
        rc, png = cv.imencode(".png", face)
        msg = png.tobytes()
        print("Publishing message to topic:", MQTT_TOPIC)
        mqttclient.publish(MQTT_TOPIC, payload=msg, qos=QOS, retain=False)

cap.release()
cv.destroyAllWindows()

mqttclient.loop_forever()

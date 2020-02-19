# w251 - Homework 03
## Internet of Things 101

### Introduction
Per the instructions of the assignment, I created an internet of things application that captures facial images and sends them to a cloud-based object storage account. In total, I created five containers to operate the different modules of the application. Dockerfiles were created to establish an image from which to launch each individual container. The three containers running locally from the Jetson and the two containers running on the virtual machine are linked through a bridged network defined in the docker run scripts for each of the containers. Descriptions of the docker containers, their functionality, and detail of the docker run scripts for each are as follows:

1. The first container, faceDet, runs the python package cv2 to connect to the USB camera, detect the coordinates of a face, and publish an encoded image to a local mosquitto broker under the topic "hw3". When running this container it necessary to add necessary to grant the container access to the camera (/dev/video0). Note: Despite the instructions indicating that video0 is reserved for the built-in camera, in my configuration video0 indeed points to the USB camera.

```docker run --name faceDet --device /dev/video0 --network hw03 hw03-facedet```

2. The second container, mqttLocBrk, is a based on a lightweight alpine image and serves to simply launch and run the mosquitto broker.

```docker run --name mqttLocBrk --network hw03 hw03-mqttlocbrk```

3. The third container, mqttLocFor, subscribes to the local broker to receive the facial images generated in the first container and subsequently forwards them to the cloud under the topic hw3_facedet.

```docker run --name mqttLocFor --network hw03 hw03-mqttLocFor```

4. The fourth container, mqttCldBrk, is identical to the second container running a basic alpine image to run the cloud-based mosquitto broker. This container runs on a virtual machine previously configured running ubuntu and docker.

```docker run --name mqttCldBrk --network hw03 hw03-mqttcldbrk```

5. The fifth and final container, imgProc, subscribes to the cloud-based mosquitto broker and writes the messages received (images) to a local directory. When launching this container it is necessary to define a volume for saving the image files which essentially links a directory in the container with a directory in the virtual machine. Note that a cloud-based block storage account was created and linked to the same directory in the virtual machine in advance, applying s3cmd.

```docker run --name imgProc --volume "/mnt/mareiter-hw03:/mnt/mareiter-hw03" --network hw03 hw03-imgproc```

In terms of the mosquitto messaging topics used, as this is a relatively basic example, with only one type of message (images) being sent and received, I used the basic topics of hw3 for the local messaging and hw_facedet for the cloud messaging. Different topics were chosen for local and cloud messages simply to monitor and debug the implementation easier. In more complex applications involving multiple types of messages and hierarchy, a more complex naming structure would be applied.

In term of the quality of service (QOS) appied for the messaging, I chose 1 (at least once) as it generated the best results in sending messages in real time and avoids message loss.

# w251 - Homework 03
## Internet of Things 101

### Introduction
Per the instructions of the assignment, I created an internet of things application that captures facial images and sends them to a cloud-based object storage account. In total, I created five containers to operate the different modules of the application. Dockerfiles were created to establish an image from which to launch each individual container. The three containers running locally from the Jetson and the two containers running on the virtual machine are linked through a bridged network defined in the docker run scripts for each of the containers. Descriptions of the docker containers, their functionality, and detail of the docker run scripts for each are as follows:

1. The first container, faceDet, runs the python package cv2 to connect to the USB camera, detect the coordinates of a face, and publish an encoded image to a local mosquitto broker. When running this container it  necessary to add necessary to grant the container access to the camera (/dev/video0). Note: Despite the instructions indicating that video0 is reserved for the built-in camera, in my configuration video0 indeed points to the USB camera.
2. The second container, mqttLocBrk is a based on a lightweight alpine image and serves to simply launch and run the mosquitto broker.
3. The third container, mqttLocFor, subscribes to the local broker to receive the facial images generated in the first container and subsequently forward them to the cloud.
4. The fourth container, mqttCldBrk, is identical to the second container running a basic alpine image to run the cloud-based mosquitto broker.
5. The fifth and final container, imgProc, subscribes to the cloud-based mosquitto broker and writes the messages received (images) to a local directory. When launching this container it is necessary to define a volume for saving the image files which essentially links a directory in the container with a directory in the virtual machine. Note that a cloud-based block storage account was created and linked to the same directory in the virtual machine in advance, applying s3cmd.

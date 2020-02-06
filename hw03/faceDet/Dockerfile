FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages 
RUN apt-get update
RUN apt-get install -y python3-opencv \
                       python3-pip \
                       libopencv-dev \
                       libcanberra-gtk3-module \
                       vim-tiny \
                       mosquitto-clients

# Install paho mqtt to send messages to broker
RUN pip3 install paho-mqtt numpy

RUN mkdir app
COPY . /app
WORKDIR /app
#RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD ["run.py" ]


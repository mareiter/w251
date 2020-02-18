FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages 
RUN apt-get update
RUN apt-get install -y python3-opencv \
                       python3-pip \
                       libopencv-dev \
                       vim-tiny \
                       mosquitto-clients

# Install paho mqtt to subscribe to messages from broker
RUN pip3 install numpy \
		 paho-mqtt

RUN mkdir app
COPY . /app
WORKDIR /app

ENTRYPOINT [ "python3" ]
CMD ["run.py" ]

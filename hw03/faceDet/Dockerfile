FROM w251/cuda:dev-tx2-4.3_b132

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
RUN pip3 install numpy \ 
		 paho-mqtt

RUN mkdir app
COPY . /app
WORKDIR /app

ENTRYPOINT [ "python3" ]
CMD ["run.py" ]

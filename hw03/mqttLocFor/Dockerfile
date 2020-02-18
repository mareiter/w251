FROM alpine

RUN apk update
RUN apk add mosquitto-clients
RUN apk add py3-paho-mqtt

RUN mkdir app
COPY . /app
WORKDIR /app

ENTRYPOINT ["python3" ]
CMD ["run.py" ]

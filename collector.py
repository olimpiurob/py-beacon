import paho.mqtt.client as mqtt
from proximity import *

def onConnect(client, userdata, rc):
    print("Connected to broker: " + str(rc))

def initMQTT(url = "localhost", port = 1883, keepalive = 60):
    client = mqtt.Client()
    client.on_connect = onConnect
    try:
        client.connect(url, port, keepalive)
        client.loop_start()
        return client
    except Exception, e:
        print(e)
        return None

def startScan(mqttclnt, filter=""):
    if mqttclnt:
        scanner = Scanner()
        while True:
            for beacon in scanner.scan():
                fields = beacon.split(",")
                if fields[1].startswith(filter):
                    mqttclnt.publish("/ble/id/" + fields[0], fields[5])

if __name__ == '__main__':
    clnt = initMQTT()
    startScan(clnt)

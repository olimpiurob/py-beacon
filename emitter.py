import paho.mqtt.client as mqtt
import time
from proximity import *

DEBUG = True
calculator = 0

def onConnect(client, userdata, rc):
    print("Connected to broker: " + str(rc))
    client.subscribe("/ble/id/#")

def onMessage(client, userdata, msg):
    # len("/ble/id/") = 8
    calculator.add(msg.topic[8:], int(msg.payload))

def initMQTT(url = "localhost", port = 1883, keepalive = 60):
    client = mqtt.Client()
    client.on_connect = onConnect
    client.on_message = onMessage
    try:
        client.connect(url, port, keepalive)
        client.loop_start()
        return client
    except Exception, e:
        print(e)
        return None

if __name__ == '__main__':
    calculator = Calculator(chkTimer = 3, threshold = 10)
    clnt = initMQTT()
    while True:
        time.sleep(3)
        ret, val = calculator.nearest()
        if ret:
            clnt.publish("/ble/nearest/", '{"id":"' + ret + '","val":'+ str(val) + '}')
            if DEBUG: print(ret, val)
        
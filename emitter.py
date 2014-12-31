#
# by Taka Wang
#

import paho.mqtt.client as mqtt
import time, ConfigParser
from proximity import *

DEBUG = True
calculator = 0
conf  = 0

def onConnect(client, userdata, rc):
    print("Connected to broker: " + str(rc))
    client.subscribe(conf["topic_id"] + "#")

def onMessage(client, userdata, msg):
    calculator.add(msg.topic[conf["topic_id_len"]:], int(msg.payload))

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

def init():
    ret = {}
    config = ConfigParser.ConfigParser()
    config.read("config")
    ret["url"]           = config.get('MQTT', 'url')
    ret["port"]          = int(config.get('MQTT', 'port'))
    ret["keepalive"]     = int(config.get('MQTT', 'keepalive'))
    ret["queueCapacity"] = int(config.get('Calculator', 'queueCapacity'))
    ret["chkTimer"]      = int(config.get('Calculator', 'chkTimer'))
    ret["threshold"]     = int(config.get('Calculator', 'threshold'))
    ret["topic_id"]      = config.get('Scanner', 'topic_id')
    ret["nearest_id"]    = config.get('Scanner', 'nearest_id')
    ret["topic_id_len"]  = len(ret["topic_id"])
    return ret

if __name__ == '__main__':
    conf = init()
    calculator = Calculator(conf["queueCapacity"], conf["chkTimer"], conf["threshold"])
    clnt = initMQTT(conf["url"], conf["port"], conf["keepalive"])
    while True:
        time.sleep(3)
        ret, val = calculator.nearest()
        if ret:
            clnt.publish(conf["nearest_id"], '{"id":"' + ret + '","val":'+ str(val) + '}')
            if DEBUG: print(ret, val)
        
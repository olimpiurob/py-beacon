#
# by Taka Wang
#

import ConfigParser
import paho.mqtt.client as mqtt
from proximity import *

DEBUG = True


def onConnect(client, userdata, rc):
    """MQTT onConnect handler"""
    print("Connected to broker: " + str(rc))


def initMQTT(url="localhost", port=1883, keepalive=60, client_id=None,
             username=None, password=None, certificate=None, client_key=None,
             client_cert=None, mqtt_protocol="3.1.1"):
    """Init MQTT connection"""
    proto = mqtt.MQTTv311
    if mqtt_protocol == "3.1":
        proto = mqtt.MQTTv31

    if not client_id:
        client = mqtt.Client(protocol=proto)
    else:
        client = mqtt.Client(client_id, protocol=proto)

    if username is not None:
        client.username_pw_set(username, password)

    if certificate is not None:
        client.tls_set(certificate, certfile=client_cert, keyfile=client_key)

    client.on_connect = onConnect
    try:
        client.connect(url, port, keepalive)
        client.loop_start()
        return client
    except Exception, e:
        print(e)
        return None


def startScan(mqttclnt, filter="", topic="/ble/rssi/"):
    """Scan BLE beacon and publish to MQTT broker"""
    if mqttclnt:
        scanner = Scanner()
        while True:
            for beacon in scanner.scan():
                fields = beacon.split(",")
                if fields[1].startswith(filter):
                    mqttclnt.publish(topic, '{"id":"%s","val":"%s"}' % (fields[0], fields[5]))
                    if DEBUG:
                        print(fields[0], fields[5])


def init():
    """Read config file"""
    ret = {}
    config = ConfigParser.ConfigParser()
    config.read("config")
    global DEBUG
    DEBUG = True if int(config.get('Collector', 'debug')) == 1 else False
    ret["url"]           = config.get('MQTT', 'url')
    ret["port"]          = int(config.get('MQTT', 'port'))
    ret["keepalive"]     = int(config.get('MQTT', 'keepalive'))
    ret["client_id"]     = config.get('MQTT', 'client_id')
    ret["username"]      = config.get('MQTT', 'username')
    ret["password"]      = config.get('MQTT', 'password')
    certificate = config.get('MQTT', 'certificate')
    client_cert = config.get('MQTT', 'client_cert')
    client_key = config.get('MQTT', 'client_key')
    ret["certificate"]   = certificate if certificate else None
    ret["client_key"]    = client_key if client_key else None
    ret["client_cert"]   = client_cert if client_cert else None
    ret["mqtt_protocol"] = config.get('MQTT', 'protocol')
    ret["filter"]        = config.get('Scanner', 'filter')
    ret["topic_id"]      = config.get('Scanner', 'topic_id')
    return ret

if __name__ == '__main__':
    conf = init()
    clnt = initMQTT(conf["url"], conf["port"], conf["keepalive"],
                    conf["client_id"], conf["username"], conf["password"],
                    conf["certificate"], conf["client_key"],
                    conf["client_cert"], conf["mqtt_protocol"])
    startScan(clnt, conf["filter"], conf["topic_id"])

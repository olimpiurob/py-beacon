#
# by Taka Wang
#

import ConfigParser
 
config = ConfigParser.ConfigParser()
config.read("config")

print(config.get('MQTT', 'url'))
print(config.get('MQTT', 'port'))
print(config.get('MQTT', 'keepalive'))
print(config.get('MQTT', 'client_id'))
print(config.get('MQTT', 'username'))
print(config.get('MQTT', 'password'))
print(config.get('MQTT', 'certificate'))
print(config.get('MQTT', 'client_key'))
print(config.get('MQTT', 'client_cert'))
print(config.get('MQTT', 'protocol'))

print(config.get('Calculator', 'queueCapacity'))
print(config.get('Calculator', 'chkTimer'))
print(config.get('Calculator', 'threshold'))

print(config.get('Scanner', 'deviceId'))
print(config.get('Scanner', 'loops'))
print(config.get('Scanner', 'filter'))
print(config.get('Scanner', 'topic_id'))
print(config.get('Scanner', 'nearest_id'))

print(config.get('Emitter', 'sleepInterval'))
print(config.get('Emitter', 'debug'))

print(config.get('Collector', 'debug'))

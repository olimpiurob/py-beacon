import blescan
import sys
import time
import paho.mqtt.client as mqtt
import bluetooth._bluetooth as bluez

dev_id = 0

try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", port=1883, keepalive=60)
client.loop_start()

while True:
	returnedList = blescan.parse_events(sock, 1)
	for beacon in returnedList:
		result = beacon.split(",")
		if result[1].startswith("64657203194"):
			client.publish("/uuid/" + result[0], result[5])
			#print beacon, int(time.time())
			#print result[0], result[5]



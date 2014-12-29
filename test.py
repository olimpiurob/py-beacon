from led import *
import time
import blescan
import sys

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

while True:
	led_all(False) # turn off
	mac = ""
	val = -200
	returnedList = blescan.parse_events(sock, 10)
	for beacon in returnedList:
		#print beacon
		result = beacon.split(",")
		if int(result[5]) > val :
			val = result[5]
			mac = result[0]
	if (mac == "52:48:d9:dd:b1:84"):
		led_a(True)
		print("IPAD:" + result[5])
	elif (mac == "d0:39:72:c3:a2:d6"):
		led_b(True)
		print("BLE MINI:" + result[5])
	else:
		print("Unknown " + result[0])
	time.sleep(0.2)


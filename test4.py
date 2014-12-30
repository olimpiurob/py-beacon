import blescan
import sys
import bluetooth._bluetooth as bluez
import datetime
from collections import deque
from numpy import average

dev_id = 0

try:
    sock = bluez.hci_open_dev(dev_id)
    print "ble thread started"

except:
    print "error accessing bluetooth device..."
        sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

blue = deque(maxlen=5)
green= deque(maxlen=5)
blue_val = -200
green_val = -200

while True:
    returnedList = blescan.parse_events(sock, 1)
    result = ""
    for beacon in returnedList:
        #print beacon
        result = beacon.split(",")
        if (result[0] == "fe:95:5c:da:63:9d"):
            green.append(int(result[5]))
        elif (result[0] == "d7:53:ea:b7:22:6a"):
            blue.append(int(result[5]))
    if (len(blue)== 5):
        blue_val = average(blue, weights=range(1,6,1))
    if (len(green) == 5):
        green_val = average(green, weights=range(1,6,1))
    if (green_val > blue_val):
        print "Green", green_val
    else:
        print "Blue", blue_val



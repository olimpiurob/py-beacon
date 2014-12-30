import paho.mqtt.client as mqtt
import sys, operator
from collections import deque
from numpy import average

uuid, rssi = {}, {}

def add(id, value):
	if (id not in uuid):
		uuid[id] = deque(maxlen=5)
		rssi[id] = -sys.maxint - 1
	uuid[id].append(value)
	if (len(uuid[id]) == 5):
		rssi[id] = average(uuid[id], weights=range(1,6,1))

def cal_max():
	for id, values in uuid.iteritems():
		if (len(values) == 5):
			max_id = max(uuid.iteritems(), key=operator.itemgetter(1))[0]
			return max_id, rssi[max_id]
	return None, None

if __name__ == "__main__":
	add("123", 1)
	add("456", 1)
	add("123", 2)
	add("567", 1)
	add("123", 3)
	add("123", 4)
	#add("123", 5)
	#add("123", 6)
	ret, val = cal_max()
	print(ret, val)
	print(uuid.keys())
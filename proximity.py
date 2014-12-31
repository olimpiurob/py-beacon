#
# by Taka Wang
#

import sys, operator, threading
from collections import deque
from numpy import average
# require by Scanner class
import blescan
import bluetooth._bluetooth as bluez

class Calculator():
    def __init__(self, qCapacity = 5, timer = 0):
        self.uid  = {}
        self.rssi = {}
        self.capacity = qCapacity # capacity for each queue
        if timer > 0:
            self.__setInterval(self.sanitize, timer)

    def __setInterval(self, func, sec):
        def func_wrapper():
            self.__setInterval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    def sanitize(self):
        print("TODO: clean missing beacons")

    def add(self, id, value):
        if (id not in self.uid):
            self.uid[id]  = deque(maxlen = self.capacity) # size limited queue
            self.rssi[id] = -sys.maxint - 1 # init with -inf

        self.uid[id].append(value)
        if (len(self.uid[id]) == self.capacity):
            # weighted moving average calculation via numpy's average function
            self.rssi[id] = average(self.uid[id], weights = range(1, self.capacity + 1, 1))
    
    def nearest(self):
        for id, container in self.uid.iteritems():
            # no matter which uid satisfy this condition, calculate the max 
            if (len(container) == self.capacity):
                max_uid = max(self.uid.iteritems(), key = operator.itemgetter(1))[0]
                return max_uid, self.rssi[max_uid]
        return None, None

    def uids(self):
        return self.uid.keys()

    def test(self):
        for i in xrange(1, 10):
            self.add("id-1", i)
        for j in xrange(1, 10, 2):
            self.add("id-2", j)
        ret, val = self.nearest()
        print(ret, val)
        print(self.uids())

class Scanner():
    def __init__(self, deviceId = 0, loops = 1):
        self.deviceId = deviceId
        self.loops = loops
        try:
            self.sock = bluez.hci_open_dev(self.deviceId)
            blescan.hci_le_set_scan_parameters(self.sock)
            blescan.hci_enable_le_scan(self.sock)
        except Exception, e:
            print e   

    def scan(self):
        return blescan.parse_events(self.sock, self.loops)

    def test(self):
        while True:
            for beacon in self.scan():
                print beacon

if __name__ == '__main__':
    c = Calculator(timer = 1)
    c.test()
    s = Scanner(loops = 3)
    s.test()

'''
from proximity import *
c = Calculator()
c.test()
s = Scanner(loops = 3)
s.test()    
''' 
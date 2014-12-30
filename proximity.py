import sys, operator
from collections import deque
from numpy import average

import blescan
import bluetooth._bluetooth as bluez

class Calculator():
    def __init__(self, steps=5):
        self.steps = steps
        self.uuid = {}
        self.rssi = {}

    def add(self, id, value):
        if (id not in self.uuid):
            self.uuid[id] = deque(maxlen=self.steps)
            self.rssi[id] = -sys.maxint - 1
        self.uuid[id].append(value)
        if (len(self.uuid[id]) == self.steps):
            self.rssi[id] = average(self.uuid[id], weights=range(1,self.steps+1,1))
    
    def nearest(self):
        for id, values in self.uuid.iteritems():
            if (len(values) == self.steps):
                max_id = max(self.uuid.iteritems(), key=operator.itemgetter(1))[0]
                return max_id, self.rssi[max_id]
        return None, None

    def uuids(self):
        return self.uuid.keys()

    def test(self):
        for i in xrange(1, 10):
            self.add("id-1", i)
        for j in xrange(1, 10, 2):
            self.add("id-2", j)
        ret, val = self.nearest()
        print(ret, val)
        print(self.uuids())

class Scanner():
    def __init__(self, dev_id=0, loops=1):
        self.dev_id = dev_id
        self.loops = loops
        try:
            self.sock = bluez.hci_open_dev(self.dev_id)
            blescan.hci_le_set_scan_parameters(self.sock)
            blescan.hci_enable_le_scan(self.sock)
        except Exception, e:
            print "error accessing bluetooth device..."
            sys.exit(1)   

    def scan(self):
        return blescan.parse_events(self.sock, self.loops)

    def test(self):
        while True:
            for beacon in self.scan():
                print beacon

if __name__ == '__main__':
    c = Calculator()
    c.test()
    s = Scanner(loops=3)
    s.test()

'''
from proximity import *
c = Calculator()
c.test()
s = Scanner(loops=3)
s.test()    
''' 
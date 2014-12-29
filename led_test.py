#!/usr/bin/python
from led import *
import time

print "LED Blink"

while True:
	led_a(True)
	led_b(True)
	time.sleep(0.5)
	led_a(False)
	led_b(False)
	time.sleep(0.5)

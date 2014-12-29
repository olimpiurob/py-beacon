#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_13", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)

def led(pin, isOn):
	if isOn:
		GPIO.output(pin, GPIO.HIGH)
	else:
		GPIO.output(pin, GPIO.LOW)

def led_a(on):
	led("P8_13", on)


def led_b(on):
	led("P8_14", on)

def led_all(on):
	led("P8_13", on)
	led("P8_14", on)
#!/usr/bin/env python3 

from ev3dev.ev3 import *
from time import sleep

us = UltrasonicSensor()

assert us.connected, "Connect a US sensor"

units = us.units
us.mode = 'US-DIST-CM'

while True:
	dist = us.value()/10 #mm to cm
	print(str(dist) + " " + units)
	if(dist <= 5) :
		Leds.set_color(Leds.LEFT, Leds.RED)
		Leds.set_color(Leds.RIGHT, Leds.RED)
	else:
		Leds.set_color(Leds.LEFT, Leds.GREEN)
		Leds.set_color(Leds.RIGHT, Leds.GREEN)

	#sleep(1)

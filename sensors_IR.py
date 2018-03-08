#!/usr/bin/env python3 

from ev3dev.ev3 import *
from time import sleep

ir = InfraredSensor()

assert ir.connected, "Connect a IR sensor"

ir.mode = 'IR-PROX'

while True:
	dist = ir.value()
	print(str(dist))
	if(dist <= 5) :
		Leds.set_color(Leds.LEFT, Leds.RED)
		Leds.set_color(Leds.RIGHT, Leds.RED)
	else:
		Leds.set_color(Leds.LEFT, Leds.GREEN)
		Leds.set_color(Leds.RIGHT, Leds.GREEN)

	#sleep(1)

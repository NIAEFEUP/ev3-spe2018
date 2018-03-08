#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep

mA = ev3.LargeMotor('outA')
mD = ev3.LargeMotor('outD')


#mA.run_timed(time_sp=10000, speed_sp=-200)
#mD.run_timed(time_sp=10000, speed_sp=200)

def turn_right():
	"""Turns right"""
	mA.run_to_rel_pos(position_sp=350, speed_sp=500, stop_action="brake")
	mD.run_to_rel_pos(position_sp=-360, speed_sp=500, stop_action="brake")
	mA.wait_while('running')
	mD.wait_while('running')

def turn_left():
	"""Turns left"""
	mA.run_to_rel_pos(position_sp=-360, speed_sp=500, stop_action="brake")
	mD.run_to_rel_pos(position_sp=360, speed_sp=500, stop_action="brake")
	mA.wait_while('running')
	mD.wait_while('running')


ev3.Sound.speak('Herique is gay').wait()

#turn_left()

#sleep(2)

turn_right()
turn_right()
turn_right()
turn_right()

ev3.Sound.beep()

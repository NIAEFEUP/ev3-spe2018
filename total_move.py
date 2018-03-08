#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

mA = LargeMotor('outA')
mD = LargeMotor('outD')

ir = InfraredSensor()
assert ir.connected, "Connect an IR sensor"

ir.mode = 'IR-PROX'

us = UltrasonicSensor()
assert us.connected, "Please connect North Korea"

us.mode = 'US-DIST-CM'

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

def set_right_motor_speed(speed):
	mA.run_forever(speed_sp=speed)

def set_left_motor_speed(speed):
	mD.run_forever(speed_sp=speed)

def stop_motor_right():
	mA.stop(stop_action="hold")

def stop_motor_left():
	mD.stop(stop_action="hold")

def get_distance_front():
	#Pass to cm
	return us.value()/10

def get_distance_right():
	return ir.value()

#Config vars
default_speed = 200
right_threshold = 5
right_factor = 3.5

def calc_right_speed():
	return default_speed + (right_threshold - get_distance_right()) * right_factor

speed_left = default_speed
speed_right = default_speed

while True:
	set_left_motor_speed(-speed_left)
	set_right_motor_speed(-speed_right)
	
	print("right_speed = " + str(speed_right) + "    left_speed = " + str(speed_left))

	if(get_distance_front() <= 2):
		speed_left = 0
		speed_right = 0
		stop_motor_left()
		stop_motor_right()
		break
	
	speed_right = calc_right_speed()

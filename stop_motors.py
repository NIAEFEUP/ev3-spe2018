#!/usr/bin/env python3

from ev3dev.ev3 import *

mA = LargeMotor('outA')
mD = LargeMotor('outD')

mA.stop(stop_action='coast')
mD.stop(stop_action='coast')

Sound.speak('Herique is gay').wait()

Sound.beep()

#!/usr/bin/python

import TB6612FNGcontroller as motor
import time

        # PWM.set_frequency(PWMB, 60)



motor.init()

# for speed in range(20, 100):
#     motor.moveBackwards(motor.Channel.RIGHT, speed)
#     motor.moveBackwards(motor.Channel.LEFT, speed)
#     time.sleep(0.02)

# motor.moveBackwards(motor.Channel.RIGHT, 0)
# motor.moveBackwards(motor.Channel.LEFT, 0)
# motor.softStop(motor.Channel.RIGHT)
# motor.softStop(motor.Channel.LEFT)
# time.sleep(2)

# for speed in range(20, 100):
#     motor.moveForward(motor.Channel.RIGHT, speed)
#     motor.moveForward(motor.Channel.LEFT, speed)
#     time.sleep(0.02)
#
#
# motor.softStop(motor.Channel.RIGHT)
# motor.softStop(motor.Channel.LEFT)
import mygetch


while(1):
    k = ord(mygetch.getch())
    print(k)
    if k==65: #up
        motor.moveForward(motor.Channel.LEFT,100)
        motor.moveForward(motor.Channel.RIGHT,100)
    elif k==66: #down
        motor.moveBackwards(motor.Channel.LEFT,100)
        motor.moveBackwards(motor.Channel.RIGHT,100)
    elif k==67: #right
        motor.moveForward(motor.Channel.LEFT,100)
        motor.moveForward(motor.Channel.RIGHT,30)
    elif k==68: #left
        motor.moveForward(motor.Channel.LEFT,30)
        motor.moveForward(motor.Channel.RIGHT,100)
    elif k==32: #space
        motor.softStop(motor.Channel.LEFT)
        motor.softStop(motor.Channel.RIGHT)
    elif k==113: #q
        break;




motor.cleanup()
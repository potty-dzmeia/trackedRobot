__author__ = 'pottry'


import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM



# Motor Controller (TB6612FNG) logic
#--------------------------------------------------
# STBY - HIGH - operational mode (should be connected to VCC)
#        LOW  - puts the controller in low power mode.
#
# AIN1            AIN2        PWMA        Function
# BIN1            BIN2        PWMB
#--------------------------------------------------
# 1               0           %           motor is rotating CW with speed proportional to PWMA
# 0               1           %           motor is rotating CCW with speed proportional to PWMA
# 0               0           N.A.        soft stop
# 1               1           N.A.        soft stop
# N.A             N.A.        0%          hard stop

#RIGHT motor
PWMA = "P9_14"
AIN1 = "P8_11"
AIN2 = "P8_12"

#LEFT motor
PWMB = "P8_19"
BIN1 = "P8_15"
BIN2 = "P8_16"

STBY = "P8_17"


class Channel:
    RIGHT = "RIGHT"
    LEFT = "LEFT"



def init():
    PWM.start(PWMA, 0, 1000, 0)
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(AIN2, GPIO.OUT)

    GPIO.setup(STBY, GPIO.OUT)

    PWM.start(PWMB, 0, 1000, 0)
    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)

    GPIO.output(STBY, GPIO.HIGH)



def cleanup():
    PWM.stop(PWMA)
    PWM.stop(PWMB)
    PWM.cleanup()

    GPIO.cleanup()

    GPIO.output(STBY, GPIO.LOW)



def moveForward(motorName, speed):
    if motorName == Channel.RIGHT:
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        PWM.set_duty_cycle(PWMA, speed)
    elif motorName == Channel.LEFT:
        GPIO.output(BIN1, GPIO.HIGH)
        GPIO.output(BIN2, GPIO.LOW)
        PWM.set_duty_cycle(PWMB, speed)
    else:
        print("Wrong motor name: LEFT or RIGHT possible only")



def moveBackwards(motorName, speed):
    if motorName == Channel.RIGHT:
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        PWM.set_duty_cycle(PWMA, speed)
    elif motorName == Channel.LEFT:
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        PWM.set_duty_cycle(PWMB, speed)
    else:
        print("Wrong motor name: LEFT or RIGHT possible only")


def hardStop(motorName):
    if motorName==Channel.RIGHT:
        PWM.set_duty_cycle(PWMA)
    elif motorName == Channel.LEFT:
        PWM.set_duty_cycle(PWMB)
    else:
        print("Wrong motor name: LEFT or RIGHT possible only")


def softStop(motorName):
    if motorName==Channel.RIGHT:
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.LOW)
    elif motorName == Channel.LEFT:
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.LOW)
    else:
        print("Wrong motor name: LEFT or RIGHT possible only")
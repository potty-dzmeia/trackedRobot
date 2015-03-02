import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import logging
import logging.config
from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))) # needed for importing misc_utils
import misc_utils

logging.config.fileConfig(misc_utils.get_logging_config(), disable_existing_loggers=False)
logger = logging.getLogger(__name__)


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



# BBB pin assignment
# ------------------
#RIGHT motor
PWMA = "P9_14"
AIN1 = "P8_11"
AIN2 = "P8_12"

#LEFT motor
PWMB = "P8_19"
BIN1 = "P8_15"
BIN2 = "P8_16"

STBY = "P8_17"


class Tb6612fn:
    """
    Driver for the Pololu motor controller board
    """

    class Channel:
        RIGHT = "RIGHT"
        LEFT = "LEFT"

    @classmethod
    def init(cls):
        PWM.start(PWMA, 0, 1000, 0)
        GPIO.setup(AIN1, GPIO.OUT)
        GPIO.setup(AIN2, GPIO.OUT)

        GPIO.setup(STBY, GPIO.OUT)

        PWM.start(PWMB, 0, 1000, 0)
        GPIO.setup(BIN1, GPIO.OUT)
        GPIO.setup(BIN2, GPIO.OUT)

        GPIO.output(STBY, GPIO.HIGH)


    @classmethod
    def cleanup(cls):
        PWM.stop(PWMA)
        PWM.stop(PWMB)
        PWM.cleanup()

        GPIO.cleanup()

        GPIO.output(STBY, GPIO.LOW)


    @classmethod
    def moveForward(cls, motorName, speed):
        if not 0 <= speed <= 100:
            logger.error("Invalid speed value")
            return

        if motorName == cls.Channel.RIGHT:
            GPIO.output(AIN1, GPIO.HIGH)
            GPIO.output(AIN2, GPIO.LOW)
            PWM.set_duty_cycle(PWMA, speed)
        elif motorName == cls.Channel.LEFT:
            GPIO.output(BIN1, GPIO.HIGH)
            GPIO.output(BIN2, GPIO.LOW)
            PWM.set_duty_cycle(PWMB, speed)
        else:
            logger.error("Wrong motor name: LEFT or RIGHT possible only")


    @classmethod
    def moveBackwards(cls, motorName, speed):
        if not 0 <= speed <= 100:
            logger.error("Invalid speed value")
            return

        if motorName == cls.Channel.RIGHT:
            GPIO.output(AIN1, GPIO.LOW)
            GPIO.output(AIN2, GPIO.HIGH)
            PWM.set_duty_cycle(PWMA, speed)
        elif motorName == cls.Channel.LEFT:
            GPIO.output(BIN1, GPIO.LOW)
            GPIO.output(BIN2, GPIO.HIGH)
            PWM.set_duty_cycle(PWMB, speed)
        else:
            logger.error("Wrong motor name: LEFT or RIGHT possible only")

    @classmethod
    def hardStop(cls, motorName):
        if motorName == cls.Channel.RIGHT:
            PWM.set_duty_cycle(PWMA)
        elif motorName == cls.Channel.LEFT:
            PWM.set_duty_cycle(PWMB)
        else:
            logger.error("Wrong motor name: LEFT or RIGHT possible only")

    @classmethod
    def softStop(cls, motorName):
        if motorName == cls.Channel.RIGHT:
            GPIO.output(AIN1, GPIO.LOW)
            GPIO.output(AIN2, GPIO.LOW)
        elif motorName == cls.Channel.LEFT:
            GPIO.output(BIN1, GPIO.LOW)
            GPIO.output(BIN2, GPIO.LOW)
        else:
            logger.error("Wrong motor name: LEFT or RIGHT possible only")
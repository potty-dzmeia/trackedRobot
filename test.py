#!/usr/bin/python
import sys
LED3_PATH = "/sys/class/leds/beaglebone:green:usr3"


def writeLED ( filename, value, path=LED3_PATH ):
    "This function writes the passed value to the file in the path"
    fo = open( path + filename,"w")
    fo.write(value)
    fo.close()
    return

def removeTrigger():
    writeLED (filename="/trigger", value="none")
    return


print "Flashing the LED"
writeLED (filename="/trigger", value="timer")
writeLED (filename="/delay_on", value="500")
writeLED (filename="/delay_off", value="500")

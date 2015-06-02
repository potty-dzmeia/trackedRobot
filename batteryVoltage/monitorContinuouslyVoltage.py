#!/usr/bin/python
__author__ = 'pottry'

import time
import measureBatteryVoltage


if __name__ == "__main__":
    
    while(1):
        time.sleep(1)
        print(measureBatteryVoltage.getVoltage())



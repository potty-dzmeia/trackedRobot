#!/usr/bin/env python2
__author__ = 'pottry'


import voiceRecognition as vc
import os

if __name__ == '__main__':

    command = vc.voiceCommand()
    command = command.lower()

    if(command == "time"):
        os.system("echo \"The time is $(date +%l) o'clock and $(date +%l) minutes\"  | festival --tts")

    elif(command == "date"):
        os.system("echo \"Today is $(date +%e) of  $(date +%B)\"  | festival --tts")

    elif(command == "battery voltage"):
        os.system("../batteryVoltage/crontTask_voltageMonitor.sh")

    else:
        os.system("echo \"Unknown command! You said: " + command + "\"""  | festival --tts")
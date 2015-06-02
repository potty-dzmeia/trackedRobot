#!/usr/bin/env python2
import os

def beep():
    os.system('aplay beep.wav 2>/dev/null&')

if __name__ == '__main__':
    beep()
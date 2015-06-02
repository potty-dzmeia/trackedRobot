#!/usr/bin/env python2
import beep as b
import voiceCommand as vc
import sys
import os


if __name__ == '__main__':


    # sys.stdout = os.devnull
    # sys.stderr = os.devnull


    #play beep sound tell us we are ready to accept voice input
    b.beep()

    print( vc.voiceCommand() )
    #os.system('./voiceCommand 2>/dev/null')


    #print(vc.voiceCommand())

    # sys.stdout = sys.__stdout__
    # sys.stderr = sys.__stderr__
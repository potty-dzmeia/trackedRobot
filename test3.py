#!/usr/bin/python

import mygetch


# PWMB = "P8_19"
#
# PWM.start(PWMB, 0)
# PWM.set_duty_cycle(PWMB, 50)
# time.sleep(3)
# PWM.cleanup()



while(1):
    k = ord(mygetch.getch())
    print(k)
    if k==65:
        print("up")
    elif k==66:
        print("down")
    elif k==67:
        print("right")
    elif k==68:
        print("left")
    elif k==32:
        print("space")
    elif k==113:
        print("q")




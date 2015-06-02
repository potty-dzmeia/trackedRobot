#!/usr/bin/python
__author__ = 'pottry'

import Adafruit_BBIO.ADC as ADC

# Voltage divider range (38KOhm - 12KOhm):
# ---------------------------------------
#  U2=0.767V (U1=3.2V) min          --> ADC = 0.41
#  U2=0.870V (U1=3.7V) average      --> ADC = 0.49
#  U2=1.000V (U1=4.2V) max          --> ADC = 0.55
#
# 3.2v --> 0.41
# 3.3  --> 0.43
# 3.4  --> 0.44
# 3.5  --> 0.46
# 3.6  --> 0.47
# 3.7  --> 0.48
# 3.8  --> 0.49
# 3.9  --> 0.51
# 4.0  --> 0.52
# 4.1  --> 0.54
# 4.2  --> 0.55
#

voltagePin = "P9_35"

adcToVoltage = {"0.41": 3.1,
                "0.42": 3.2,
                "0.43": 3.3,
                "0.44": 3.4,
                "0.45": 3.4,
                "0.46": 3.5,
                "0.47": 3.6,
                "0.48": 3.7,
                "0.49": 3.8,
                "0.50": 3.8,
                "0.51": 3.9,
                "0.52": 4.0,
                "0.53": 4.0,
                "0.54": 4.1,
                "0.55": 4.2,
                "0.56": 4.3,}

MEASURE_POINTS = 10


def getVoltage():

    ADC.setup()
    adc = 0.0

    for i in range(MEASURE_POINTS) :
        adc = adc + ADC.read(voltagePin)

    adc /= MEASURE_POINTS

    if adc<0.405:
        return "low"
    if adc>0.565:
        return "high"

    adc = "{0:.2f}".format(adc)



    try:
        voltage = adcToVoltage[adc]
    except:
        return "error"


    return str(voltage)


if __name__ == "__main__":

    print(getVoltage())





#!/usr/bin/python
import serial
import socket
import sys
from baud_rates import BaudRates
from keys_status import KeysStatus

# Receives serial data (bluetooth) from RoboRemo and sends it to the UDP process responsible for moving the robot

def sendUDP(to_socket, to_address, msg):
    # Send data
    print >> sys.stderr, 'sending "%s"' % msg
    sent = to_socket.sendto(msg, to_address)



ROBOREMO_MESSAGE_REPEAT_PERIOD = 0.1  # When a button is hold on the app a message will be sent repeatedly every XXXms


# ------------ Serial Port ------------#
ser = serial.Serial('/dev/ttyUSB0', baudrate=BaudRates.B_115200, xonxoff=False,
                    rtscts=False, dsrdtr=False, timeout=ROBOREMO_MESSAGE_REPEAT_PERIOD)
ser.flushInput()
ser.flushOutput()

# ------------ UDP ------------#
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.0.104', 10000)


keys_status = 0

while True:

    data = ser.read(1)  # Read from com port with time out of 0.1sec

    # Timeout - reset the keys_status to empty
    if not data:
        keys_status = 0

    # We have data, so send it to UDP movement thread
    else:
        print("incoming serial data: {}".format(data))
        data = int(data)
        if data == 1:
            keys_status |= KeysStatus.UP
        elif data == 2:
            keys_status &= ~KeysStatus.UP
        elif data == 3:
            keys_status |= KeysStatus.DOWN
        elif data == 4:
            keys_status &= ~KeysStatus.DOWN
        elif data == 5:
            keys_status |= KeysStatus.LEFT
        elif data == 6:
            keys_status &= ~KeysStatus.LEFT
        elif data == 7:
            keys_status |= KeysStatus.RIGHT
        elif data == 8:
            keys_status &= ~KeysStatus.RIGHT
        elif data == 9:
            keys_status |= KeysStatus.SPEED_UP
        else:
            print >> sys.stderr, "unknown command: {}".format(keys_status)

        print("sending data: {}".format(keys_status))
        sendUDP(sock, server_address, str(keys_status))







    # bytesToRead = ser.inWaiting()
    # bytes = ser.read(bytesToRead)
    # if bytesToRead>0:
    #     print(bytes)

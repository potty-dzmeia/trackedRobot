#!/usr/bin/python
import serial
import socket
import sys
import logging
import logging.config
import signal
import config as cfg
from keys_status import KeysStatus
import misc_utils

logging.config.fileConfig(misc_utils.get_logging_config(), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# Process that receives serial data (bluetooth) from RoboRemo and after
# short processing sends it to the movement_udp.py process (which is responsible
# for moving the robot)
#


#
def sendUDP(to_socket, to_address, msg):
    logger.info('{} ----> UDP'.format(msg))
    to_socket.sendto(msg, to_address)


#
def stop_roboremo_gracefully(sig, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    sock.close()
    print('Pressed crt+c')
    logger.warning('roboremo_serial_to_udp.py is closing! Received signal: {}'.format(sig))
    sys.exit(0)


#
def run_program():

    keys_status = 0

    while True:
        data = ser.read(1)  # Read from com port with time out of ROBOREMO_MESSAGE_REPEAT_PERIOD (0.1sec)

        # Timeout - reset the keys_status to empty
        if not data:
            keys_status = 0

        # We have data, so send it to UDP movement thread
        else:
            logger.info('incoming serial ---> : {}'.format(data))

            try:
                data = int(data)
            except Exception as exc:
                logger.error(exc)
                continue

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
                logger.error('unknown command: {}'.format(keys_status))

            sendUDP(sock, server_address, str(keys_status))
            keys_status &= ~KeysStatus.SPEED_UP # clear the speed-up command

#
if __name__ == '__main__':
    # store the original SIGINT handler, which will be restored in stop_roboremo_gracefully()
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, stop_roboremo_gracefully)

    # ------------ Serial Port for receiving commands from RoboRemo app ------------#
    ser = serial.Serial(cfg.BLUETOOTH_TO_SERIAL_DEV_NAME,
                        baudrate=cfg.BLUETOOTH_TO_SERIAL_BAUD_RATE,
                        xonxoff=False, rtscts=False, dsrdtr=False,
                        timeout=cfg.ROBOREMO_MESSAGE_REPEAT_PERIOD)
    ser.flushInput()
    ser.flushOutput()

    # ------------ UDP  for sending the commands to the movement_udp process------------#
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (cfg.MOVEMENT_UDP_IP_ADDRESS, cfg.MOVEMENT_UDP_LISTENS_ON_PORT)

    run_program()


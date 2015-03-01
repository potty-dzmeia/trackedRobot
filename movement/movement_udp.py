#!/usr/bin/python
import socket
import sys
import Queue
from threading import Thread
from keys_status import KeysStatus
from tracked_vehicle_controller import TrackedVehicleController
import misc_utils
import logging

logging.config.fileConfig(misc_utils.get_logging_config(), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

UDP_PORT = 10000
MY_ADDRESS = "0.0.0.0"



#
def movementThread(msg_queue):
    """
    The thread reads from the message queue and steers the vehicle for up to 100ms with the the command that
    was received. A command is needed every 100ms if we want to keep the vehicle moving (i.e. in case of empty msg
    queue the vehicle stops).
    New command will overwrite the previous.

    :param msg_queue: Queue containing KeysStatus in string form
    :type msg_queue: Queue.Queue
    :return:
    """

    MOVEMENT_TIMEOUT = 0.2

    vehicle = TrackedVehicleController()

    last_read_was_empty = True    # True if queue was empty the last time we tried to read from it

    while True:

        try:
            # read the queue:
            #  - generate an exception if empty
            #  - block for 100ms if the last read was empty
            key_code = msg_queue.get(block=last_read_was_empty, timeout=MOVEMENT_TIMEOUT)

            #logger.info("got KeysCode: " + key_code)
            last_read_was_empty = False
            movement, speed = KeysStatus.convertToVehicleCommands(int(key_code)) # we received a command - move the vehicle for 100ms in the selected direction
            vehicle.set(movement, speed)

        except Queue.Empty:
            if last_read_was_empty:  # Stop the vehicle if we didn't get a command for 100ms
                logger.info("Movement timeout - stopping vehicle")
                vehicle.stop()
            last_read_was_empty = True


# Start listening for UDP packets containing KeysCode
# Any KeysStatus bytes will be redirected to the movementThread which is responsible of steering the vehicle
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a TCP/IP socket

    server_address = (MY_ADDRESS, UDP_PORT) # Bind the socket to the port
    logger.info('Starting up on %s port %s' % server_address)
    sock.bind(server_address)

    queue = Queue.Queue()

    movement_thread = Thread(target=movementThread, args=(queue,))
    movement_thread.start()


    while True:
        logger.info('waiting to receive message')
        data, address = sock.recvfrom(4096)

        logger.info('received %s bytes from %s' % (len(data), address))
        logger.info(data)

        queue.put_nowait(data)

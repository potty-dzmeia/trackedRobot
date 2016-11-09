#!/usr/bin/python
import socket
import config as cfg
import Queue
from threading import Thread
from keys_status import KeysStatus
from tracked_vehicle_controller import TrackedVehicleController
import misc_utils
import logging
import signal
import sys
import time
import logging.config

logging.config.fileConfig(misc_utils.get_logging_config(), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# Process responsible of moving the robot.
# Input: bytes of the type KeysStatus coming through the UDP
# Output: Robot movement


MOVEMENT_TIMEOUT = 0.2


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
    vehicle = TrackedVehicleController()

    last_read_was_empty = True    # True if queue was empty the last time we tried to read from it

    while True:

        try:
            # read the queue:
            #  - generate an exception if empty
            #  - block for 100ms if the last read was empty
            key_code = msg_queue.get(block=last_read_was_empty, timeout=MOVEMENT_TIMEOUT)

            if key_code == KeysStatus.QUIT:
                logger.warning('movement_udp.py: movementThread is finished')
                return

            last_read_was_empty = False
            movement, speed = KeysStatus.convertToVehicleCommands(int(key_code)) # we received a command - move the vehicle for 100ms in the n
            vehicle.set(movement, speed)
            logger.info("Vehicle command was set successfully")

        except Queue.Empty:
            if last_read_was_empty:  # Stop the vehicle if we didn't get a command for 100ms
                logger.debug("movement_udp.py: Movement timeout - stopping vehicle")
                vehicle.stop()
            last_read_was_empty = True
        except:
            logger.error("movement_udp.py: Unexpected error:", sys.exc_info()[0])



#
def stop_movement_udp_gracefully(sig, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    queue.put_nowait(KeysStatus.QUIT) # Tell the thread to quit
    logger.warning('movement_udp.py: is closing! Received signal: {}'.format(sig))
    time.sleep(1)
    sock.close()

    sys.exit(0)


# Start listening for UDP packets containing KeysCode
# Any KeysStatus bytes will be redirected to the movementThread which is responsible of steering the vehicle
if __name__ == "__main__":
    queue = Queue.Queue()

    # store the original SIGINT handler, which will be restored in stop_roboremo_gracefully()
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, stop_movement_udp_gracefully)

    # ------------ UDP  for receiving commands------------#
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a TCP/IP socket
    server_address = (cfg.MOVEMENT_UDP_IP_ADDRESS, cfg.MOVEMENT_UDP_LISTENS_ON_PORT) # Bind the socket to the port
    logger.info('movement_udp.py: Starting up on %s port %s' % server_address)
    sock.bind(server_address)

    # Start the thread which will take care of moving the vehicle
    movement_thread = Thread(target=movementThread, args=(queue,))
    movement_thread.start()

    while True:
        logger.info('movement_udp.py: Waiting to receive UDP message')
        data, address = sock.recvfrom(4096)

        logger.info('movement_udp.py: Received %s bytes from %s' % (len(data), address))
        logger.info('movement_udp.py: data = {}'.format(data))

        queue.put_nowait(data)

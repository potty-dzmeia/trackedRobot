import socket
import sys
import time
import Queue
from threading import Thread
from keycodes_to_vehicle_commands import KeyCodesToVehicleCommands
from tracked_vehicle_controller import TrackedVehicleController
import misc_utils
import logging

logging.config.fileConfig(misc_utils.get_logging_config(), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

UDP_PORT = 10000
MY_ADDRESS = "192.168.0.104"



def movementThread(msg_queue):
    """
    The thread reads from the message queue and steers the vehicle for up to 100ms with the the command that was received
    If a new command will overwrite the previous.
    In case of empty msg queue the vehicle stops.

    :param msg_queue: key code that needs to be translated to vehicle command
    :type msg_queue: Queue.Queue
    :return:
    """

    vehicle = TrackedVehicleController()

    bLastReadWasEmpty = True    # True if queue was empty the last time we tried to read from it

    while True:

        try:
            key_code = msg_queue.get(block=bLastReadWasEmpty, timeout=0.1)   # read the queue - generate exception if empty
            print "got message: " + key_code
            bLastReadWasEmpty = False
            movement, speed = KeyCodesToVehicleCommands.convert(int(key_code)) # we received a command - move the vehicle for 100ms in the selected direction
            vehicle.set(movement, speed)

        except Queue.Empty:
            bLastReadWasEmpty = True



#
# def udpThread(msg_queue):
#     """
#     The thread reads incoming
#     :param msg_queue:
#     :type msg_queue: Queue.Queue
#     :return:
#     """


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.0.104', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

queue = Queue.Queue()

movement_thread = Thread(target=movementThread, args=(queue,))
movement_thread.start()


while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)

    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data

    queue.put_nowait(data)
import socket
import sys
import time




def movementThread(msg_queue):
    """

    :param msg_queue:
    :
    :return:
    """
    while


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.0.104', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)

    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data

    time.sleep(5)

    # if data:
    #     sent = sock.sendto(data, address)
    #     print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
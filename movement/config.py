from baud_rates import BaudRates

ROBOREMO_MESSAGE_REPEAT_PERIOD = 0.1  # When a button is hold on the app a message will be sent repeatedly every XXXms
MOVEMENT_UDP_IP_ADDRESS = '0.0.0.0'
MOVEMENT_UDP_LISTENS_ON_PORT = 10000
BLUETOOTH_TO_SERIAL_BAUD_RATE = BaudRates.B_38400
BLUETOOTH_TO_SERIAL_DEV_NAME = '/dev/ttyUSB0'
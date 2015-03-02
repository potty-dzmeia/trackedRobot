__author__ = 'potty'


class UdpVehicleMessage:
    """
    Contains the message (keys code) and the address that it is coming from
    """

    def __init__(self, from_address, key_code):
        self.__key_code = key_code
        self.__from_adress = from_address


    def getKeyCode(self):
        return self.__key_code

    def getFromAddress(self):
        return self.__from_adress




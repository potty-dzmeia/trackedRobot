
class Movement:
    """
    Gives the direction of vehicle movement depending on the current keys being pressed
    """


    class State:
        """Possible states of the vehicle"""
        FORWARD             = 1
        FORWARD_LEFT        = 2
        FORWARD_RIGHT       = 3
        FORWARD_STOPPING    = 4
        STOPPED             = 5
        STOPPED_LEFT        = 6
        STOPPED_RIGHT       = 7
        BACKWARDS           = 8
        BACKWARDS_LEFT      = 9
        BACKWARDS_RIGHT     = 10
        BACKWARDS_STOPPING  = 11


    class Keys:
        UP      = 0b00001
        DOWN    = 0b00010
        LEFT    = 0b00100
        RIGHT   = 0x01000
        BRAKE   = 0x10000


    __keyStatus = 0 # tells us which keys are being pressed. It is a number resulting from adding the values from Keys class
    __vehicleState = State.STOPPED; # The current state of the vehicle


    def keyPressed(self, key, bPressed):
        """
        Function to be called when a key is pressed in order to control the movement of the vehicle
        :param key: Variable of the type Movement.Keys
        :param bPressed: True if the key is pressed, False if is being depressed
        :return:
        """
        if key == self.Keys.UP:
            self.__keyStatus =  self.__keyStatus && bPressed
        elif key == self.Keys.DOWNP:
            self.__bDOWN = bPressed
        elif key == self.Keys.LEFT:
            self.__bUP = bPressed
        elif key == self.Keys.RIGHT:
            self.__bRIGHT = bPressed

        __calculateNewState()



    def getSate(self):
        """
        Returns the current state of the vehicle (e.g. FORWARD or FORWARD_RIGHT or BACKWARDS_RIGHT...)
        :return: variable of the type Movement.State
        """
        return self.__vehicleState



    def __calculateNewState(self):
        """
         Calculates the current state of the vehicle depending on the keys that are being pressed.
        """

        # STOP
        if self.__BRAKE == True:
            self.__vehicleState = self.State.STOPPED

        # FORWARD
        elif self.__bUP == True:
            self.__vehicleState = self.State.FORWARD

        # FORWARD_LEFT
        elif






    
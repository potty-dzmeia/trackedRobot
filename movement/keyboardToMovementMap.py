import movementTypes as movementType

class KeyboardToMovement:
    """
    Gives the direction of vehicle movement depending on the current keys being pressed
    """
    class Keys:
        UP          = 0b00000001
        DOWN        = 0b00000010
        LEFT        = 0b00000100
        RIGHT       = 0b00001000
        BRAKE       = 0b00010000
        QUIT        = 0b00100000
        SPEED_UP    = 0b01000000
        SPEED_DOWN  = 0b10000000


    @staticmethod
    def calculateNewState(keysStatus):
        """
         Calculates the current state of the vehicle depending on the keys that are being pressed.
        """
        command = movementType.SOFT_STOP
        speed   = movementType.SPEED_NO_CHANGE

        if keysStatus & KeyboardToMovement.Keys.SPEED_UP:
            speed = movementType.SPEED_UP
            keysStatus = keysStatus & ~KeyboardToMovement.Keys.SPEED_UP # clear the speed bit not to mixup the logic below
        elif keysStatus & KeyboardToMovement.Keys.SPEED_DOWN:
            speed = movementType.SPEED_DOWN
            keysStatus = keysStatus & ~KeyboardToMovement.Keys.SPEED_DOWN # clear the speed bit not to mixup the logic below


        # HARD_STOP
        if keysStatus & KeyboardToMovement.Keys.BRAKE:
            command = movementType.HARD_STOP

        # FORWARD
        elif keysStatus == KeyboardToMovement.Keys.UP:
            command =  movementType.FORWARD

        # FORWARD_LEFT
        elif keysStatus == KeyboardToMovement.Keys.UP | KeyboardToMovement.Keys.LEFT:
            command =  movementType.FORWARD_LEFT

        # FORWARD_RIGHT
        elif keysStatus == KeyboardToMovement.Keys.UP | KeyboardToMovement.Keys.RIGHT:
            command =  movementType.FORWARD_RIGHT

        # LEFT_WHILE_STOPPED
        elif keysStatus == KeyboardToMovement.Keys.LEFT:
            command =  movementType.LEFT_WHILE_STOPPED

        # RIGHT_WHILE_STOPPED
        elif keysStatus == KeyboardToMovement.Keys.RIGHT:
            command =  movementType.RIGHT_WHILE_STOPPED

        # BACKWARDS
        elif keysStatus == KeyboardToMovement.Keys.DOWN:
            command =  movementType.BACKWARDS

        # BACKWARDS_LEFT
        elif keysStatus == KeyboardToMovement.Keys.DOWN | KeyboardToMovement.Keys.LEFT:
            command =  movementType.BACKWARDS_LEFT

        # BACKWARDS_RIGHT
        elif keysStatus == KeyboardToMovement.Keys.DOWN | KeyboardToMovement.Keys.RIGHT:
            command =  movementType.BACKWARDS_RIGHT

        # SOFT_STOP - if no direction is selected
        else:
            command =  movementType.SOFT_STOP




        return command, speed


    @staticmethod
    def __isMoving(keysStatus):

        bIsMoving = keysStatus & (KeyboardToMovement.Keys.UP   | \
                                  KeyboardToMovement.Keys.DOWN | \
                                  KeyboardToMovement.Keys.LEFT | \
                                  KeyboardToMovement.Keys.RIGHT)

        return bIsMoving

    
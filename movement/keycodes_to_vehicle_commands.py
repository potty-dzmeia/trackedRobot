from tracked_vehicle_controller import TrackedVehicleController


class KeyCodesToVehicleCommands:
    """
    Gives the direction of vehicle movement depending on the current keys being pressed
    """


    class KeyCodes:
        UP          = 0b00000001
        DOWN        = 0b00000010
        LEFT        = 0b00000100
        RIGHT       = 0b00001000
        BRAKE       = 0b00010000
        QUIT        = 0b00100000
        SPEED_UP    = 0b01000000
        SPEED_DOWN  = 0b10000000


    @classmethod
    def convert(cls, keyCode):
        """
        Calculates the command that must be send to the vehicle depending on the keys that are being pressed.

        :param keyCode: 8bit value - for the meaning of each bit see class Keys
        :type command: int
        :return: Vehicle commands: direction of movement and Speed
        """


        # Determine the speed command
        # -------------------------------
        speed_command = TrackedVehicleController.SpeedCommands.SPEED_NO_CHANGE

        if keyCode & cls.KeyCodes.SPEED_UP:
            speed_command = TrackedVehicleController.SpeedCommands.SPEED_UP
            keyCode = keyCode & ~cls.KeyCodes.SPEED_UP # clear the speed bit not to mix up the logic below
        elif keyCode & cls.KeyCodes.SPEED_DOWN:
            speed_command = TrackedVehicleController.SpeedCommands.SPEED_DOWN
            keyCode = keyCode & ~cls.KeyCodes.SPEED_DOWN # clear the speed bit not to mix up the logic below


        # Determine the direction command
        # -------------------------------
        direction_command = TrackedVehicleController.DirectionCommands.SOFT_STOP

        # HARD_STOP
        if keyCode & cls.KeyCodes.BRAKE:
            direction_command = TrackedVehicleController.DirectionCommands.HARD_STOP

        # FORWARD
        elif keyCode == cls.KeyCodes.UP:
            direction_command =  TrackedVehicleController.DirectionCommands.FORWARD

        # FORWARD_LEFT
        elif keyCode == cls.KeyCodes.UP | KeyCodesToVehicleCommands.KeyCodes.LEFT:
            direction_command =  TrackedVehicleController.DirectionCommands.FORWARD_LEFT

        # FORWARD_RIGHT
        elif keyCode == cls.KeyCodes.UP | KeyCodesToVehicleCommands.KeyCodes.RIGHT:
            direction_command =  TrackedVehicleController.DirectionCommands.FORWARD_RIGHT

        # LEFT_WHILE_STOPPED
        elif keyCode == cls.KeyCodes.LEFT:
            direction_command =  TrackedVehicleController.DirectionCommands.LEFT_WHILE_STOPPED

        # RIGHT_WHILE_STOPPED
        elif keyCode == cls.KeyCodes.RIGHT:
            direction_command =  TrackedVehicleController.DirectionCommands.RIGHT_WHILE_STOPPED

        # BACKWARDS
        elif keyCode == cls.KeyCodes.DOWN:
            direction_command =  TrackedVehicleController.DirectionCommands.BACKWARDS

        # BACKWARDS_LEFT
        elif keyCode == cls.KeyCodes.DOWN | cls.KeyCodes.LEFT:
            direction_command =  TrackedVehicleController.DirectionCommands.BACKWARDS_LEFT

        # BACKWARDS_RIGHT
        elif keyCode == cls.KeyCodes.DOWN | cls.KeyCodes.RIGHT:
            direction_command =  TrackedVehicleController.DirectionCommands.BACKWARDS_RIGHT

        # SOFT_STOP - if no direction is selected
        else:
            direction_command =  TrackedVehicleController.DirectionCommands.SOFT_STOP


        return direction_command, speed_command



    @classmethod
    def __isMoving(cls, keysStatus):

        bIsMoving = keysStatus & (KeyCodesToVehicleCommands.KeyCodes.UP   | \
                                  KeyCodesToVehicleCommands.KeyCodes.DOWN | \
                                  KeyCodesToVehicleCommands.KeyCodes.LEFT | \
                                  KeyCodesToVehicleCommands.KeyCodes.RIGHT)

        return bIsMoving

    
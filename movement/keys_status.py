from tracked_vehicle_controller import TrackedVehicleController


class KeysStatus:
    """
    A KeysStatus is a 1byte value which describes the buttons which are being currently pressed by the user
    """

    UP          = 0b00000001
    DOWN        = 0b00000010
    LEFT        = 0b00000100
    RIGHT       = 0b00001000
    BRAKE       = 0b00010000
    QUIT        = 0b00100000
    SPEED_UP    = 0b01000000
    SPEED_DOWN  = 0b10000000


    @classmethod
    def convertToVehicleCommands(cls, keys_status):
        """
        Converts a KeysStatus into a command that can be send to the TrackedVehicleController class

        :param keys_status: 8bit value - for the meaning of each bit see class Keys
        :type command: int
        :return: Vehicle commands: direction of movement and speed
        """

        # Determine the speed command
        # -------------------------------
        speed_command = TrackedVehicleController.SpeedCommands.SPEED_NO_CHANGE

        if keys_status & cls.SPEED_UP:
            speed_command = TrackedVehicleController.SpeedCommands.SPEED_UP
            keys_status &= ~cls.SPEED_UP  # clear the speed bit not to mix up the logic below
        elif keys_status & cls.SPEED_DOWN:
            speed_command = TrackedVehicleController.SpeedCommands.SPEED_DOWN
            keys_status &= ~cls.SPEED_DOWN  # clear the speed bit not to mix up the logic below

        # Determine the direction command
        # -------------------------------
        # HARD_STOP
        if keys_status & cls.BRAKE:
            direction_command = TrackedVehicleController.DirectionCommands.HARD_STOP
        # FORWARD
        elif keys_status == cls.UP:
            direction_command = TrackedVehicleController.DirectionCommands.FORWARD
        # FORWARD_LEFT
        elif keys_status == cls.UP | cls.LEFT:
            direction_command = TrackedVehicleController.DirectionCommands.FORWARD_LEFT
        # FORWARD_RIGHT
        elif keys_status == cls.UP | cls.RIGHT:
            direction_command = TrackedVehicleController.DirectionCommands.FORWARD_RIGHT
        # LEFT_WHILE_STOPPED
        elif keys_status == cls.LEFT:
            direction_command = TrackedVehicleController.DirectionCommands.LEFT_WHILE_STOPPED
        # RIGHT_WHILE_STOPPED
        elif keys_status == cls.RIGHT:
            direction_command = TrackedVehicleController.DirectionCommands.RIGHT_WHILE_STOPPED
        # BACKWARDS
        elif keys_status == cls.DOWN:
            direction_command = TrackedVehicleController.DirectionCommands.BACKWARDS
        # BACKWARDS_LEFT
        elif keys_status == cls.DOWN | cls.LEFT:
            direction_command = TrackedVehicleController.DirectionCommands.BACKWARDS_LEFT
        # BACKWARDS_RIGHT
        elif keys_status == cls.DOWN | cls.RIGHT:
            direction_command = TrackedVehicleController.DirectionCommands.BACKWARDS_RIGHT
        # SOFT_STOP - if no direction is selected
        else:
            direction_command = TrackedVehicleController.DirectionCommands.SOFT_STOP

        return direction_command, speed_command
from tb6612fng_driver import Tb6612fn
import misc_utils
import logging
import logging.config

logging.config.fileConfig(misc_utils.get_logging_config(), disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class TrackedVehicleController:
    """
    First init() and then use the set() method to set the direction and the speed of the vehicle
    """

    class DirectionCommands:
        """Possible commands controlling the direction of movement"""
        FORWARD             = 1
        FORWARD_LEFT        = 2
        FORWARD_RIGHT       = 3
        LEFT_WHILE_STOPPED  = 4
        RIGHT_WHILE_STOPPED = 5
        BACKWARDS           = 6
        BACKWARDS_LEFT      = 7
        BACKWARDS_RIGHT     = 8
        HARD_STOP           = 9
        SOFT_STOP           = 10



    class SpeedCommands:
        """
        Possible commands controlling the speed
        """
        SPEED_UP            = 11
        SPEED_DOWN          = 12
        SPEED_NO_CHANGE     = 13


    LOWEST_SPEED  = 0.3
    HIGHEST_SPEED = 1.0
    SPEED_STEPS   = 0.1


    def __init__(self):
        Tb6612fn.init()
        self.speed = self.LOWEST_SPEED  # Init to lowest speed


    def __del__(self):
        Tb6612fn.cleanup()


    def stop(self):
        """
        Stops the vehicle using SOFT stop
        :return:
        """
        Tb6612fn.softStop(Tb6612fn.Channel.LEFT)
        Tb6612fn.softStop(Tb6612fn.Channel.RIGHT)
        self.speed = self.LOWEST_SPEED


    def set(self, direction, speed):
        """
        Sets the direction of movement and speed of the vehicle

        :param direction: Command controlling the direction of movement
        :type direction: int
        :param speed: Command controlling the speed of movement
        :type speed: int
        """

        logger.info("direction_cmd: " + str(direction)+"; speed_cmd: " + str(speed))
    
        # Update current speed
        # --------------------
        if speed == self.SpeedCommands.SPEED_UP:
            self.speed += self.SPEED_STEPS
            if self.speed>self.HIGHEST_SPEED:
                self.speed = self.HIGHEST_SPEED

        elif speed == self.SpeedCommands.SPEED_DOWN:
            self.speed -= self.SPEED_STEPS
            if self.speed<self.LOWEST_SPEED:
                self.speed = self.LOWEST_SPEED

        # Tell the two electric motors what to do 
        # --------------------
        if direction == self.DirectionCommands.FORWARD:
            Tb6612fn.moveForward(Tb6612fn.Channel.LEFT, 100*self.speed)
            Tb6612fn.moveForward(Tb6612fn.Channel.RIGHT,93*self.speed)

        elif direction == self.DirectionCommands.FORWARD_LEFT:
            Tb6612fn.moveForward(Tb6612fn.Channel.LEFT, 35*self.speed)
            Tb6612fn.moveForward(Tb6612fn.Channel.RIGHT,100*self.speed)

        elif direction == self.DirectionCommands.FORWARD_RIGHT:
            Tb6612fn.moveForward(Tb6612fn.Channel.LEFT, 100*self.speed)
            Tb6612fn.moveForward(Tb6612fn.Channel.RIGHT,35*self.speed)

        elif direction == self.DirectionCommands.LEFT_WHILE_STOPPED:
            Tb6612fn.moveForward(Tb6612fn.Channel.RIGHT, 100*self.speed)
            Tb6612fn.moveBackwards(Tb6612fn.Channel.LEFT,100*self.speed)

        elif direction == self.DirectionCommands.RIGHT_WHILE_STOPPED:
            Tb6612fn.moveBackwards(Tb6612fn.Channel.RIGHT, 100*self.speed)
            Tb6612fn.moveForward(Tb6612fn.Channel.LEFT,100*self.speed)

        elif direction == self.DirectionCommands.BACKWARDS:
            Tb6612fn.moveBackwards(Tb6612fn.Channel.LEFT, 100*self.speed)
            Tb6612fn.moveBackwards(Tb6612fn.Channel.RIGHT,100*self.speed)

        elif direction == self.DirectionCommands.BACKWARDS_LEFT:
            Tb6612fn.moveBackwards(Tb6612fn.Channel.LEFT, 35*self.speed)
            Tb6612fn.moveBackwards(Tb6612fn.Channel.RIGHT,100*self.speed)

        elif direction == self.DirectionCommands.BACKWARDS_RIGHT:
            Tb6612fn.moveBackwards(Tb6612fn.Channel.LEFT, 100*self.speed)
            Tb6612fn.moveBackwards(Tb6612fn.Channel.RIGHT,35*self.speed)

        elif direction == self.DirectionCommands.SOFT_STOP:
            Tb6612fn.softStop(Tb6612fn.Channel.LEFT)
            Tb6612fn.softStop(Tb6612fn.Channel.RIGHT)
            self.speed = self.LOWEST_SPEED

        elif direction == self.DirectionCommands.HARD_STOP:
            Tb6612fn.hardStop(Tb6612fn.Channel.LEFT)
            Tb6612fn.hardStop(Tb6612fn.Channel.RIGHT)
            self.speed = self.LOWEST_SPEED


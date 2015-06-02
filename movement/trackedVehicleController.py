import TB6612FNGcontroller as motorCtrl
import movementTypes as movementTypes

class TrackedVehicleController:

    LOWEST_SPEED  = 0.3
    HIGHEST_SPEED = 1.0
    SPEED_STEPS   = 0.1



    def __init__(self):
        motorCtrl.init()
        self.speed = self.LOWEST_SPEED

    def __del__(self):
        motorCtrl.cleanup()

    def setCommand(self, command, speedCommand):
        """
        Sets the direction of movement
        :param command: integer defined in movementTypes.py
        :param speed: integer defined in movementTypes.py
        :return:
        """

        print "command " + str(command)
        print "speedCommand " + str(speedCommand)

        if speedCommand == movementTypes.SPEED_UP:
            self.speed = self.speed + self.SPEED_STEPS
            if self.speed>self.HIGHEST_SPEED:
                self.speed = self.HIGHEST_SPEED

        elif speedCommand == movementTypes.SPEED_DOWN:
            self.speed = self.speed - self.SPEED_STEPS
            if self.speed<self.LOWEST_SPEED:
                self.speed = self.LOWEST_SPEED




        if command == movementTypes.FORWARD:
            #print("forward"+str(self.speed))
            motorCtrl.moveForward(motorCtrl.Channel.LEFT, 100*self.speed)
            motorCtrl.moveForward(motorCtrl.Channel.RIGHT,93*self.speed)

        elif command == movementTypes.FORWARD_LEFT:
            motorCtrl.moveForward(motorCtrl.Channel.LEFT, 35*self.speed)
            motorCtrl.moveForward(motorCtrl.Channel.RIGHT,100*self.speed)

        elif command == movementTypes.FORWARD_RIGHT:
            motorCtrl.moveForward(motorCtrl.Channel.LEFT, 100*self.speed)
            motorCtrl.moveForward(motorCtrl.Channel.RIGHT,35*self.speed)

        elif command == movementTypes.LEFT_WHILE_STOPPED:
            motorCtrl.moveForward(motorCtrl.Channel.RIGHT, 100*self.speed)
            motorCtrl.moveBackwards(motorCtrl.Channel.LEFT,100*self.speed)

        elif command == movementTypes.RIGHT_WHILE_STOPPED:
            motorCtrl.moveBackwards(motorCtrl.Channel.RIGHT, 100*self.speed)
            motorCtrl.moveForward(motorCtrl.Channel.LEFT,100*self.speed)

        elif command == movementTypes.BACKWARDS:
            motorCtrl.moveBackwards(motorCtrl.Channel.LEFT, 100*self.speed)
            motorCtrl.moveBackwards(motorCtrl.Channel.RIGHT,100*self.speed)

        elif command == movementTypes.BACKWARDS_LEFT:
            motorCtrl.moveBackwards(motorCtrl.Channel.LEFT, 35*self.speed)
            motorCtrl.moveBackwards(motorCtrl.Channel.RIGHT,100*self.speed)

        elif command == movementTypes.BACKWARDS_RIGHT:
            motorCtrl.moveBackwards(motorCtrl.Channel.LEFT, 100*self.speed)
            motorCtrl.moveBackwards(motorCtrl.Channel.RIGHT,35*self.speed)

        elif command == movementTypes.SOFT_STOP:
            motorCtrl.softStop(motorCtrl.Channel.LEFT)
            motorCtrl.softStop(motorCtrl.Channel.RIGHT)
            print("lowest soft")
            self.speed = self.LOWEST_SPEED

        elif command == movementTypes.HARD_STOP:
            motorCtrl.hardStop(motorCtrl.Channel.LEFT)
            motorCtrl.hardStop(motorCtrl.Channel.RIGHT)
            print("lowest hard")
            self.speed = self.LOWEST_SPEED


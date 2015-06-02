#!/usr/bin/python
import keyboardToMovementMap as mpr
import trackedVehicleController as controller



if __name__ == "__main__":

    f = open('myfile','w')

    trackedVehicle = controller.TrackedVehicleController()


    while(1):

        keysStatus = raw_input()
        f.write(keysStatus+'\n') # python will convert \n to os.linesep
        keysStatus = int(keysStatus)


        if(keysStatus == mpr.KeyboardToMovement.Keys.QUIT):
            break;
        movement, speed = mpr.KeyboardToMovement.calculateNewState(keysStatus)
        trackedVehicle.setCommand(movement, speed)



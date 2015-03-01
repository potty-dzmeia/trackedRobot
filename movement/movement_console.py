#!/usr/bin/python
from keys_status import KeysStatus
from tracked_vehicle_controller import TrackedVehicleController
import logging
import logging.config
import misc_utils

logging.config.fileConfig(misc_utils.get_logging_config(), disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# Script for moving the vehicle using the console input


if __name__ == "__main__":

    # f = open('myfile','w')

    vehicle = TrackedVehicleController()

    while(1):

        keys_status = raw_input()
        # f.write(keysStatus+'\n') # python will convertToVehicleCommands \n to os.linesep
        keys_status = int(keys_status)

        if keys_status == KeysStatus.QUIT:
            break

        movement, speed = KeysStatus.convertToVehicleCommands(keys_status)
        vehicle.set(movement, speed)



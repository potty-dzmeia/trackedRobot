#!/usr/bin/python
from keycodes_to_vehicle_commands import KeyCodesToVehicleCommands
from tracked_vehicle_controller import TrackedVehicleController
import logging
import logging.config
import misc_utils

logging.config.fileConfig(misc_utils.get_logging_config(), disable_existing_loggers=False)
logger = logging.getLogger(__name__)


if __name__ == "__main__":

    # f = open('myfile','w')

    vehicle = TrackedVehicleController()

    while(1):

        keysStatus = raw_input()
        # f.write(keysStatus+'\n') # python will convert \n to os.linesep
        keysStatus = int(keysStatus)

        if keysStatus == KeyCodesToVehicleCommands.KeyCodes.QUIT:
            break

        movement, speed = KeyCodesToVehicleCommands.convert(keysStatus)
        vehicle.set(movement, speed)



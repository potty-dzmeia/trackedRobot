import os
import logging

logger = logging.getLogger(__name__)

def get_logging_config():
    """Returns the absolute path to the logging config file
    """

    # Now we can return the absolute path to the logging file
    path = os.path.realpath(__file__)
    a, b = os.path.split(path)
    path = os.path.join(a, "logging.conf")

    #make sure that the logger configuration file exists
    if not os.path.exists(path):
        logger.error("logging.conf was not found! We were searching in: " + path)

    return path


print get_logging_config
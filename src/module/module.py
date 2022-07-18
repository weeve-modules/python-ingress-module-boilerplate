"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""
from random import seed, randint, randrange
from time import sleep

from logging import getLogger
from api.send_data import send_data
from .params import PARAMS

log = getLogger("module")

TEMP_TOP = 30
TEMP_BOTTOM = 20
TEMP_STEP = 0.1
HUMIDITY_TOP = 100
HUMIDITY_BOTTOM = 0

def module_main():
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    try:
        seed()

        while True:
            temp_data = randint(TEMP_BOTTOM, TEMP_TOP)
            humidity_data = randint(HUMIDITY_BOTTOM, HUMIDITY_TOP)
            # input_data are data received by the module
            input_data = {
                PARAMS['TEMP_LABEL']: temp_data,
                PARAMS['HUMIDITY_LABEL']: humidity_data,
            }

            # ----------------------------------------------------------------

            # send data to the next module
            send_error = send_data(input_data)

            if send_error:
                log.error(send_error)
            else:
                log.debug("Data sent sucessfully.")

            sleep(PARAMS['SLEEP_INTERVAL'])

    except Exception as e:
        log.error(f"Exception in the module business logic: {e}")

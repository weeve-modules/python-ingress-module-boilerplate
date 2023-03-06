"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""
from logging import getLogger
from os import getenv
from time import sleep
from api.send_data import send_data
from smbus2 import smbus2 as smbus

MILL_PER_SEC = 1000

log = getLogger("module")

I2Cbus = smbus.SMBus(int(getenv("I2C_INTERFACE_NUMBER")))

if getenv("DATA_TYPE") != "byte" and getenv("DATA_TYPE") != "word":
    log.error("Invalid data type. Must be 'byte' or 'word'.")
    exit(1)
read_func = getattr(I2Cbus, "read_" + str(getenv("DATA_TYPE")) + "_data")


def module_main():
    log.info("Reading data from I2C bus " + getenv("DATA_TYPE") + "wise...")

    while True:
        data = read_func(int(getenv("SLAVE_ADDR")), int(getenv("OFFSET")))
        log.debug("Read data: ", data)

        # send data to the next module
        send_error = send_data({"i2cData": data})

        if send_error:
            log.error(send_error)
        else:
            log.debug("Data sent sucessfully.")

        sleep(int(getenv("PERIOD")) / MILL_PER_SEC)

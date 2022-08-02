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

MELL_PER_SEC = 1000
I2Cbus = smbus.SMBus(int(getenv('I2C_INTERFACE_NUMBER')))
log = getLogger("module")

def module_main():
    #Device_Address=int(getenv('SLAVE_ADDR'))
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Inputting data...")
    while True:
        # incoming i2c byte from slave
        if str(getenv('DATA_TYPE')) == "byte" :
            byte_i2c = I2Cbus.read_byte_data(int(getenv('SLAVE_ADDR')), int(getenv('OFFSET')))
            byte_i2c_data = {"i2cData": byte_i2c}
            print("I2C byte :  ",byte_i2c_data)
            # send data to the next module
            send_error = send_data(byte_i2c_data)

            if send_error:
                log.error(send_error)
            else:
                log.debug("Data sent sucessfully.")
         # incoming i2c word from slave
        elif str(getenv('DATA_TYPE')) == "word" :
            word_i2c = I2Cbus.read_word_data(int(getenv('SLAVE_ADDR')), int(getenv('OFFSET')))
            word_i2c_data = {"i2cData": word_i2c }
            print("I2C word :  ",word_i2c_data)
            # send data to the next module
            send_error = send_data(word_i2c_data)

            if send_error:
                log.error(send_error)
            else:
                log.debug("Data sent sucessfully.")
        sleep(int(getenv('PERIOD'))/ONE_THOUSAND)

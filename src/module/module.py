"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""
from os import getenv
from logging import getLogger
from api.send_data import send_data
from time import sleep
from bluepy.btle import Scanner

log = getLogger("module")
DEVICE_NAME = 9
DEVICE_MANUF_DATA = 255

def module_main():
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Inputting data...")


    while True:
        scanner = Scanner()
        devices = scanner.scan(float(getenv('SCAN_TIMEOUT')),passive = True)
        if not devices:
            OSError(
            'No nearby Devices found. Make sure your Bluetooth Connection '
            'is on.')
        for dev in devices:
            #The manufacturer data is advertized data in ble like deice name
            # should be maximum of 50 digits if the device name is composed of 2 or fewer digits
            #Digits could be the hex conversion of any or many of [0,1,2,3,4,5,6,7,8,9,1,b,c,d,e.f]
            # the letters in the last list could be upper case also
            if dev.addr == getenv('MAC_ADDR'):
                print("device name ", dev.getValueText(DEVICE_NAME))
                manuf_data = dev.getValueText(DEVICE_MANUF_DATA)
                bluetooth_data = {'bleData': str(manuf_data) }
                print("ble Data",bluetooth_data)

                # ----------------------------------------------------------------

                # input_data are data received by the module
                input_data = bluetooth_data

                # ----------------------------------------------------------------

                # send data to the next module
                send_error = send_data(input_data)

                if send_error:
                    log.error(send_error)
                else:
                    log.debug("Data sent sucessfully.")
        sleep(int(getenv('PERIOD')))

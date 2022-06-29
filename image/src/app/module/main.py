
from app.weeve.egress import send_data
from app.config import APPLICATION
from bluepy.btle import Scanner
"""
All logic related to the module's main application
Mostly only this file requires changes
"""
def module_main():
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    """
    Finds ,filter by mac address and returns the advertised ble data found
    """
    scanner = Scanner()
    devices = scanner.scan(APPLICATION['SCAN_TIMEOUT'])
    if len(devices) < 1:
        raise OSError(
            'No nearby Devices found. Make sure your Bluetooth Connection '
            'is on.')
    else:
        for dev in devices:
            #The manufacturer data is advertized data in ble like deice name should be maximum 50 digits if the device name composed by 2 or less digits
            #Digits could be the hex ocnversion of any or many of [0,1,2,3,4,5,6,7,8,9,1,b,c,d,e.f] ,the letters in the last list could be upper case also
            manufData=dev.getValueText(255)
            if dev.addr==APPLICATION['MAC_ADDR']:
                    print("device name ", dev.getValueText(9))
                    print("ble data: ", manufData)
                    sent=send_data(manufData)
                    if sent:
                        print("The data successfully sent")
                    else :
                        print("Failed to send the data")

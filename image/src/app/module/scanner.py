from bluepy.btle import Scanner
def find_ble_data_by_mac_address():
    """
    Finds ,filter by mac address and returns the advertised ble data found
    """
    scanner = Scanner()
    #The scan() methode parametre will be venv
    devices = scanner.scan(20.0)
    if len(devices) < 1:
        raise OSError(
            'No nearby Devices found. Make sure your Bluetooth Connection '
            'is on.')
    else:
        for dev in devices:
            #The manufacturer data is advertized data in ble like deice name should be maximum 50 digits if the device name composed by 2 or less digits
            #Digits could be the hex ocnversion of any or many of [0,1,2,3,4,5,6,7,8,9,1,b,c,d,e.f] ,the letters in the last list could be upper case also
            manufData=dev.getValueText(255)
            print(dev.addr)
            #the mac address bellow will be venv
            if dev.addr=='c8:c9:a3:c7:62:96':
                    print("mac address: ",dev.addr)
                    print("ble data: ", manufData)
                    return manufData
print(find_ble_data_by_mac_address(),"\n")
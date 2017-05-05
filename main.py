# this program will periodically scan nearby wifi networks
# it will display some of the networks with the strongest signal on the OLED Expansion
# it will then append info from all detected networks to a csv file

import helpers
from time import sleep

N_STRONGEST_NETWORKS = 6
SCAN_INTERVAL = 5

fieldLengths = {
    "ssid": 16,
    "signalStrength": 5,
    "gpsCoordinates": 9
}

errors = {
    "gpsNotLocked": "GPS signal is not locked. The program will try again shortly."
}

# get the directory where to save the csv file
dirName = os.path.dirname(os.path.abspath(__file__))
filename = '/'.join([dirName, 'wifiData.csv'])

def __main__():
    while True:
        # scan the wifi networks and sort by signal strength
        networks = helpers.scanWifi()
        sortedNetworks = helpers.sortNetworks(networks)
        
        # get the current gps coordinates
        gps = helpers.readGps()
        
        # if the gps read was not successful, try again from the beginning
        if not gps:
            helpers.displayError(errors["gpsNotLocked"])
            sleep(SCAN_INTERVAL)
            continue
        
        # write to screen
        helpers.displayNetworks(
            gps,
            sortedNetworks[:N_STRONGEST_NETWORKS],
            fieldLengths
        )
        
        # append to csv
        helpers.writeCsv(filename, gps, networks)
        
        # sleep
        sleep(SCAN_INTERVAL)
    
if __name__ == '__main__':
    __main__()
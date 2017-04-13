import helpers
from time import sleep

N_STRONGEST_NETWORKS = 6
SCAN_INTERVAL = 5

fieldLengths = {
    "ssid": 16,
    "signalStrength": 5,
    "gpsCoordinates": 9
}

filename = "./wifiData.csv"

def __main__():
    while True:
        # scan the wifi networks and sort by signal strength
        networks = helpers.scanWifi()
        sortedNetworks = helpers.sortNetworks(networks)
        
        # get the current gps coordinates
        gps = helpers.readGps()
        
        # write to screen
        helpers.printWifiOled(
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
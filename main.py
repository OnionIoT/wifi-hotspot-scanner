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
        networks = helpers.scanWifi()["results"]
        sortedNetworks = helpers.sortNetworks(networks)
        
        # get thecurrent gps coordinates
        gps = helpers.readGps()
        
        # write to screen
        screenOutput = helpers.prepareDisplay( 
            gps, 
            sortedNetworks[:N_STRONGEST_NETWORKS], 
            fieldLengths
        )
        helpers.oled.writeLines(screenOutput)
        
        # append to csv
        csvHeaders = ["date", "latitude", "longitude", "ssid", "bssid", "signalStrength"]
        csvRows = []
        for network in networks:
            csvRows.append({
                "date": "date",
                "latitude": gps["latitude"],
                "longitude", gps["longitude"],
                "ssid": network["ssid"],
                "bssid": network["bssid"],
                "signalStrength": network["signalStrength"]
            })
        helpers.csv.write(filename, csvRows, csvHeaders)
        
        sleep(SCAN_INTERVAL)
    
if __name__ == '__main__':
    __main__()
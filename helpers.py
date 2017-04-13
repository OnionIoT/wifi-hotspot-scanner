import ubusHelper as ubus
import oledHelper as oled
import csvHelper as csv
import shellHelper as shell
import datetime
import json

# scan wifi networks in range
# returns a list of wifi dictionaries
def scanWifi():
    device = json.dumps({"device": "ra0"})
    args = ["onion", "wifi-scan", device]
    return ubus.call(args)["results"]

# read the GPS expansion
# returns a dictionary with gps info
def readGps():
    args =["gps", "info"]
    return ubus.call(args)

# build a date time header for the top of the screen
# returns a string
def buildDateTimeHeader():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d : %X")

# sort networks by signal strength
# returns a list of network dictionaries
def sortNetworks(networks):
    return sorted(
        networks, 
        key=lambda network: int(network["signalStrength"]), 
        reverse=True
    )

# print to the display
# no return value
def printWifiOled(gps, networks, fieldLengths):
    # build a time header at the top of the screen
    timeHeader = buildDateTimeHeader()
    
    # create a list of rows of text
    # include gps data on 2nd line
    screenOutput = [
        timeHeader,
        gps["latitude"].ljust(fieldLengths["gpsCoordinates"]) + ", " + gps["longitude"].ljust(fieldLengths["gpsCoordinates"])
    ]
    
    # add the network entries
    for i in range(0, len(networks)):
        entry = networks[i]["ssid"].ljust(fieldLengths["ssid"]) + (networks[i]["signalStrength"] + "%").rjust(fieldLengths["signalStrength"])
        screenOutput.append(entry)
        
    oled.writeLines(screenOutput)
    
# write wifi network data to csv
# no return value
def writeCsv(filename, gps, networks):
    # get the current date and time
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d : %X")
    
    # build the headers and an empty row list to add to
    csvHeaders = ["date", "latitude", "longitude", "ssid", "bssid", "encryption", "signalStrength"]
    csvRows = []
    
    # append row data
    for network in networks:
        csvRows.append({
            "date": now,
            "latitude": gps["latitude"],
            "longitude": gps["longitude"],
            "ssid": network["ssid"],
            "bssid": network["bssid"],
            "encryption": network["encryption"],
            "signalStrength": network["signalStrength"]
        })
        
    # write to file
    csv.write(filename, csvRows, csvHeaders)
import ubusHelper as ubus
import oledHelper as oled
import csvHelper as csv
import datetime
import json

# scan wifi networks in range
def scanWifi():
    device = json.dumps({"device": "ra0"})
    args = ["onion", "wifi-scan", device]
    return ubus.call(args)

# read the GPS expansion
def readGps():
    args =["gps", "info"]
    return ubus.call(args)

# build a date time header for the top of the screen
def buildDateTimeHeader():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d : %X")

# sort networks by signal strength
def sortNetworks(networks):
    return sorted(
        networks, 
        key=lambda network: int(network["signalStrength"]), 
        reverse=True
    )

# build payload for display
def prepareDisplay(gps, networks, fieldLengths):
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
        
    return screenOutput
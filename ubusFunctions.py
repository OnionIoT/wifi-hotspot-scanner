# list of functions that need to make ubus calls

import ubusHelper as ubus
import json

def readGps():
    args =["gps", "info"]
    return ubus.call(args)

def scanWifi():
    device = json.dumps({"device": "ra0"})
    args = ["onion", "wifi-scan", device]
    return ubus.call(args)
    
if __name__ == '__main__':
    print "Testing ubus functions"
    print json.dumps(readGps())
    print json.dumps(scanWifi())
#/usr/bin/env python

import urllib2
import json

#GET STATION DATA
#TODO: make this a function
f = urllib2.urlopen('http://api.openweathermap.org/data/2.5/station?id=10394&APPID=d8755aae4c6f122f9184662a5abef441')
# formatted_to_json = f.readlines()[2:-2]
# print formatted_to_json
# file_contents = json.loads(str(formatted_to_json))
# print file_contents
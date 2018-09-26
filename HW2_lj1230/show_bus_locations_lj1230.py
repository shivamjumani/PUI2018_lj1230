# 2018 Fall PUI Evening Session HW3 task3: MTA BUS Location
# Author: Junru Lu, NYU, September 2018
# Usage: python show_bus_locations_lj1230.py <MTA_KEY> <BUS_LINE>

# the next line import packages that change the python 2 print function
# so that it require the same syntax as python 3
# thus the code will work both in python 2 and python 3
from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
# the next import allows me to read line input arguments
import sys

# this line checks how many arguments are passed to python
# the arguments are stored in sys.argv which is a list
# the first argument is the name of the code
# so sys.argv is a list with at least one element
# with your arguments in input it will be a list of 3
# if you add less than or more than 2 words as argument it will give you an error as well
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_lj1230.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

# this line is the url that used for requesting MTA data through provided arguments
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1]  + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]

if 'VehicleActivity' not in bus_data:
    print("Invalid BUS LINE")
else:
    bus_records = bus_data['VehicleActivity']
    # print bus line name, number of buses and their specific activities
    print("Bus Line : " + sys.argv[2])
    print("Number of Active Buses : " + str(len(bus_records)))
    for record_index in range(len(bus_records)):
        location = bus_records[record_index]['MonitoredVehicleJourney']['VehicleLocation']
        print("Bus " + str(record_index) + " is at latitude " + str(location['Latitude']) + " and longitude " + str(location['Longitude']))

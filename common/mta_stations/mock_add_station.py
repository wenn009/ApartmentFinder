from geopy.distance import vincenty
import json

MAX_TRANSIT_DIST = 2 # kilometers

newport_ri = (41.49008, -71.312796)



station_json_data = open('./station_geo.json').read()
stations = json.loads(station_json_data)

for station in stations:
    location = (station[0], station[1])
    print(vincenty(newport_ri, location).meters)
    
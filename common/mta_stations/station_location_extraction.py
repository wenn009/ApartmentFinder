import json

with open('./mtaStation.json') as station_file:
    stations = json.load(station_file)

station_geo_location = []

for station in stations['data']:
    station_geo_location.append(station[11][6:])

with open('station_geo.json', 'w') as f:
     json.dump(station_geo_location, f)
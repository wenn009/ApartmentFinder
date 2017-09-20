import json

with open('./mtaStation.json') as station_file:
    stations = json.load(station_file)

station_geo_locations = []

for station in stations['data']:
    #station_geo_location.append(station[11][7:-1])
    station_geo = station[11][7:-1].split(" ")
    station_geo_locations.append(station_geo)

with open('station_geo.json', 'w') as f:
     json.dump(station_geo_locations, f)
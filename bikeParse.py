import json
#pretty print
from pprint import pprint

json_data = open("bikeParkingShort.json")


data = json.load(json_data)
locations_list = []



for bike_rack in data["data"]:
	lat = float(bike_rack[18])
	lon = float(bike_rack[19])
	locations = {}
	locations["latitude"] = lat
	locations["longitude"] = lon
	locations_list.append(locations)

print locations_list





#parse json.data for each element[i[18][19]]
#18 & 19 are the lat/long coordinates for the bike racks
#make new bikeParkingParsed json file with full data

import json,httplib

json_data = open("bikeParkingShort.json")


data = json.load(json_data)
locations_list = []

for bike_rack in data["data"]:
	locations_list.append({
		"latitude": float(bike_rack[18]),
		"longitude": float(bike_rack[19])
	})

print locations_list





#parse json.data for each element[i[18][19]]
#18 & 19 are the lat/long coordinates for the bike racks
#make new bikeParkingParsed json file with full data

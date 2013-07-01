import json
#pretty print
from pprint import pprint

json_data = open("bikeParkingShort.json")


data = json.load(json_data)
#returning error saying "value error: extra data: line 1 column7 - end of doc"



#parse json.data for each element[i[18][19]]
#18 & 19 are the lat/long coordinates for the bike racks
#make new bikeParkingParsed json file with full data
import json,httplib

json_data = open("bikeParkingShort.json")
data = json.load(json_data)

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()

for bike_rack in data["data"]:
  connection.request('POST', '/1/classes/bikeParking', json.dumps({
                     "latitude": float(bike_rack[18]),
                     "longitude": float(bike_rack[19])
                  }), {
  "X-Parse-Application-Id": "xSId1N6iguBFx6Neo3arIQ0M206c491XdMS8T2V5",
  "X-Parse-REST-API-Key": "Xjv8hhYF1IsVcCnTggigPYowP7wc3KwW1Xdm18TZ",
  "Content-Type": "application/json"
  })
  result = json.loads(connection.getresponse().read())
  print result
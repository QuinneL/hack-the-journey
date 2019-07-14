import json
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="TOTO")

class Location:
  address = ""
  name = ""
  long_lat = (0,0)
  category = ""
  tags = []
  time_estimate = (9, 8)
  hours = 1
  def __init__(self, name, long_lat, category, tags):
    self.name = name
    self.long_lat = long_lat
    self.category = category
    self.tags = tags 
    location = geolocator.reverse(long_lat)
    self.address = location
  def __init__(self, name):
    self.name = name
  def add_time(self, time, hours):
    self.time_estimate = time
    self.hours = hours

'''
amadeus: parses through the json file that amadeus creates
returns: returns a hashmap or table 
'''
def parseAmadeus(amadeus):
  amadeus_array = json.loads(amadeus.read())
  list_locations = []
  for l in amadeus_array:
    #creating new location 
    new_location = Location(l["name"])
    list_locations.append(new_location)

  #println using for debugging only
  for item in list_locations:
    print(item.name)


#running the method on a tester
with open('j.json') as json_file: 
  parseAmadeus(json_file)

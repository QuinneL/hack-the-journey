import json
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="TOTO")
from datetime import datetime, time, date 

class Location:
  #address = ""
  name = ""
  long_lat = (0,0)
  category = ""
  tags = []
  open_time = time(hour=9)
  close_time = time(hour=20)
  hours_spent_average = 1
  price = 30
  value_out_of_hundred = 50
  def __init__(self, name, long_lat, category, tags):
    self.name = name
    self.long_lat = long_lat
    self.category = category
    self.tags = tags 
    #location = geolocator.reverse(long_lat)
    #self.address = location
  def add_time(self, open, close, price, hours):
    self.open_time = open
    self.close_time = close
    self.hours_spent_average = hours
    self.price = price
  def set_value(self, val):
    self.value_out_of_hundred = val
  #def compare_dist(self, otherlocation):    

'''
amadeus: the list returned by amadeus api
returns: returns a hashmap or table 
'''
def parseAmadeus(amadeus):
  list_locations = []
  for l in amadeus:
    #creating new location 
    long_lat = (l["geoCode"]["latitude"], l["geoCode"]["longitude"])
    list_locations.append(Location(l["name"], long_lat, l["category"], l["tags"]))

  #println using for debugging only
  for item in list_locations:
    print(item.name)

  return list_locations


#running the method on a tester
#with open('j.json') as json_file: 
#  parseAmadeus(json_file)

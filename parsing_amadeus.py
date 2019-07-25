import json
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="TOTO")
from datetime import datetime, time, date 

class Location:
  #address = ""
  name = ""
  lat_long = (0,0)
  category = ""
  tags = []
  open_time = time(hour=9)
  close_time = time(hour=20)
  hours_spent_average = 1
  price = 2
  def __init__(self, name, ll, category, tags):
    self.name = name
    self.lat_long = ll
    self.category = category
    self.tags = tags 
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
    ll = (l["geoCode"]["latitude"], l["geoCode"]["longitude"])
    list_locations.append(Location(l["name"], ll, l["category"], l["tags"]))

  #println using for debugging only
  for item in list_locations:
    print(item.name)

  return list_locations

'''
location_list: An array of Location objects
returns: an array of Location names
'''
def grabNames(location_list):
  location_names = []
  for location in location_list:
    location_names.append(location.name)
  return location_names

#running the method on a tester
#with open('j.json') as json_file: 
#  parseAmadeus(json_file)

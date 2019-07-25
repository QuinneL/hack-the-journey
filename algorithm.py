from parsing_amadeus import Location
from parsing_json import UserProfile
import math
from math import sin, cos, sqrt, atan2, radians

'''
returns the km distance between 2 lat/long locations
'''
def get_distance(location1, location2): 
    latdiff = radians(location1[0]) - radians(location2[0])
    longdiff = radians(location1[1]) - radians(location2[1])
    temp = (  
         math.sin(latdiff / 2) ** 2 
       + math.cos(location2[0]) 
       * math.cos(location1[0]) 
       * math.sin(longdiff / 2) ** 2
    )
    return 6373.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp)))

'''
locations: list of location items
profile: profile item that we will be using for creating values
returns: a version of it where each item has a numerical value and weight 
'''
def createValueList(locations_list, profile, trip):
  values = []
  weights = []
  hotel_location = trip.lat_long
  for l in locations_list:
    if l.category != "RESTAURANT":
      value_of_l = 50
      distance = abs(get_distance(hotel_location, l.lat_long))
      if l.category in profile.hobbies:
        value_of_l = value_of_l + 10
      if distance > 2:
        #assuming average driving time 
        time_to_travel = distance/25
      else:
        #assuming walking time
        time_to_travel = distance * (1/6)
      weights.append(l.hours_spent_average + int(time_to_travel))
      values.append(value_of_l)
    else:
      values.append(0)
      weights.append(100)
  return (values, weights)

def returnFoodList(locations_list):
    restaurants = []
    for loc in locations_list:
      if loc.category == "RESTAURANT":
        restaurants.append(loc)
    return restaurants 
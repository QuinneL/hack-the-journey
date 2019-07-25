from parsing_amadeus import Location
from parsing_json import UserProfile

'''
locations: list of location items
profile: profile item that we will be using for creating values
returns: a version of it where each item has a numerical value and weight 
'''
def createValueList(locations_list, profile, trip):
  values = []
  weights = []
  for l in locations_list:
    if l.category != "RESTAURANT":
      value_of_l = 50
      if l.category in profile.hobbies:
        value_of_l = value_of_l + 10
      weights.append(l.hours_spent_average)
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
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
    value_of_l = 50
    if l.category in profile.hobbies:
      value_of_l = value_of_l + 10
    weights.append(l.hours_spent_average)
    values.append(value_of_l)

  return (values, weights)


'''
valueList: a list where each item has a value and a weight
returns: a set of items that are MOST valuable but still under weight
'''
def knapsack(valueList):
    return []


'''
eventsList: list of items of class location 
trip: information about the trip
returns: a final itinenrary :D
'''
def sortByTime(eventsList,trip):
  days = []

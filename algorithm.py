from parsing_amadeus import Location
from parsing_json import UserProfile

'''
locations: list of location items
profile: profile item that we will be using for creating values
returns: a version of it where each item has a numerical value and weight 
'''
def createValueList(locations_list, profile):
  for l in locations_list:
    if l.category in profile.hobbies:
     print("YES")
     l.set_value(l.value_out_of_hundred + 10)

'''
valueList: a list where each item has a value and a weight
returns: a set of items that are MOST valuable but still under weight
'''
def knapsack(valueList):
    return []


'''
eventsList: takes in the events chosen by our algorithm
returns: a final itinenrary :D
'''
def sortByTime(eventsList):
    return []


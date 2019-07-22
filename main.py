from amadeus import Client, ResponseError
from parsing_amadeus import parseAmadeus, Location
from datetime import datetime, time, date 
from algorithm import createValueList
from parsing_json import parseProfile, UserProfile  

amadeus = Client(
    client_id='CEQgUXrPgPn5oG6KFk2BF2hvqlaZh8I3',
    client_secret='jqLjs9tEeSC41aiK'
)

#in real life the app would fetch information
profile_file = input('Name of profile json file: ')
trip_file = input('Name of trip json file: ')

#hardcoding right now
trip_lat = 41.397158
trip_long = 2.160873
city_radius = 2

try:
    response = amadeus.reference_data.locations.points_of_interest.get(latitude=trip_lat, longitude=trip_long, radius=city_radius)
except ResponseError as error:
    print(error)

locations_list = parseAmadeus(response.data)
profile = parseProfile('templateJSONS/onboarding.json')
createValueList(locations_list, profile)

'''
Creates a value/weight dictionary
The value in our case will represent events
assign weights depending on cost
'''
def createEventCost():

'''
Creates a value/weight dictionary
The value in this case will represent events
assign weights depending on user rating
'''
def createEventRating():


'''
Creates a list of events in descending order
using the knapsack method
'''
def createEventWeight()



'''

'''
result = []
def knapsack(n, value, cost, weights):
    if n == 0 or cost == 0:
        return
    else if weight[n] > cost:
        result = knapsack(n-1, cost)
    else:
        # don't put it in the knapsack
        tmp1 = knapsack(n-1,cost)
        # add it to the knapsack 
        tmp2 = value[n] + knapsack(n-1, c-weight[n])
        result.append(max{tmp1, tmp2})
    
    '''
    We have n events that the user can pick from and we 
    have a budget. Determine how we will select the events
    using knapsack algorithm
    '''

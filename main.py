from amadeus import Client, ResponseError
from parsing_amadeus import grabNames, parseAmadeus, Location
from datetime import datetime, time, date 
from algorithm import createValueList, returnFoodList
from parsing_json import parseProfile, UserProfile, UserTrip, parseUserTrip
import knapsack
import numpy as np

amadeus = Client(
    client_id='CEQgUXrPgPn5oG6KFk2BF2hvqlaZh8I3',
    client_secret='jqLjs9tEeSC41aiK'
)

locations_list = []
kp_info = []
values_list = []
weights_list = []
weight_limit = []

#in real life the app would fetch information
profile_file = input('Name of profile json file: ')
if profile_file == "":
    profile_file = 'templateJSONS/onboarding.json'
trip_file = input('Name of trip json file: ')
if trip_file == "":
    trip_file = 'templateJSONS/trip.json'

profile = parseProfile(profile_file)
trip = parseUserTrip(trip_file)
#hardcoding right now
trip_lat = trip.lat_long[0]
trip_long = trip.lat_long[1]
city_radius = 1
try:
    response = amadeus.reference_data.locations.points_of_interest.get(
        latitude=trip_lat, 
        longitude=trip_long,
        radius=city_radius
        )
except ResponseError as error:
    print(error)

locations_list.append(parseAmadeus(response.data))
kp_info.append(createValueList(locations_list[0], profile, trip))
values_list.append(kp_info[0][0])
weights_list.append(kp_info[0][1])
weight_limit.append(profile.hours_awake() * trip.num_days())

i = 0
while amadeus.next(response) is not None:
    try:
        i+=1
        response = amadeus.next(response)
        locations_list.append(parseAmadeus(response.data))
        kp_info.append(createValueList(locations_list[i], profile, trip))
        values_list.append(kp_info[i][0])
        weights_list.append(kp_info[i][1])
        weight_limit.append(profile.hours_awake() * trip.num_days())
        print(response)
    except ResponseError as error:
        print(error)
    


'''
Creates a top recommendation list of events for the user in addition to less 
personalized events list 
'''
def create_recommended_lists():
    top_recommendation_indices = knapsack.printknapSack(3 , weights_list, 
    values_list, len(values_list))
    all_recommendations = np.array(locations_list)
    top_recommendations = all_recommendations[top_recommendation_indices]

    all_indices = []
    for i in range(len(locations_list)):
        all_indices.append(i)
    
    if np.array_equal(all_indices, top_recommendation_indices):
        other_recommendations = []
    else:
        # grab the rest of the indices that were not picked by the knapsack algo
        other_recommendations_indices = np.setdiff1d(all_indices, 
                                        top_recommendation_indices)
        other_recommendations = all_recommendations[other_recommendations_indices]

    print('top_recommendations\n', grabNames(top_recommendations))
    print('other_recommendations\n', grabNames(other_recommendations))
    print('dining_recommendations\n', grabNames(returnFoodList(locations_list)))

create_recommended_lists()

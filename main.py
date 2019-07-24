from amadeus import Client, ResponseError
from parsing_amadeus import parseAmadeus, Location
from datetime import datetime, time, date 
from algorithm import createValueList
from parsing_json import parseProfile, UserProfile, UserTrip, parseUserTrip
import knapsack
import numpy as np

amadeus = Client(
    client_id='CEQgUXrPgPn5oG6KFk2BF2hvqlaZh8I3',
    client_secret='jqLjs9tEeSC41aiK'
)

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
city_radius = 10

try:
    response = amadeus.reference_data.locations.points_of_interest.get(latitude=trip_lat, longitude=trip_long, radius=city_radius)
except ResponseError as error:
    print(error)

locations_list = parseAmadeus(response.data)
kp_info = createValueList(locations_list, profile, trip)
values_list = kp_info[0]
weights_list = kp_info[1]

def create_recommended_lists():
    top_recommendation_indices = knapsack.printknapSack()
    all_recommendations = np.array(locations_list)
    top_recommendations = all_recommendations[top_recommendation_indices]

    all_indices = []
    for i in range(len(locations_list)):
        all_indices.append(i)

    other_recommendations_indices = [x for x in all_indices if x not in 
    top_recommendation_indices]
    other_recommendations = all_recommendations[other_recommendations_indices]

    return top_recommendations, other_recommendations


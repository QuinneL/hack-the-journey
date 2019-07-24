from amadeus import Client, ResponseError
from parsing_amadeus import parseAmadeus, Location
from datetime import datetime, time, date 
from algorithm import createValueList
<<<<<<< HEAD
from parsing_json import parseProfile, UserProfile, UserTrip, parseUserTrip
=======
from parsing_json import parseProfile, UserProfile
import knapsack
import numpy as np
>>>>>>> 4a6f2a4085b95c96b2b876fad745f20f00261cdc

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
trip = parseUserTrip('templateJSONS/trip.json')
print(trip.lat_long)
kp_info = createValueList(locations_list, profile, trip)

values_list = kp_info[1]
weights_list = kp_info[2]

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


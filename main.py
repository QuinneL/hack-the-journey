from amadeus import Client, ResponseError
from parsing_amadeus import parseAmadeus, Location
from datetime import datetime, time, date 

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

parseAmadeus(response.data)

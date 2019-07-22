from amadeus import Client, ResponseError
# from apiclient import discovery
from googleplaces import GooglePlaces, types, lang


# amadeus = Client(
#     client_id='CEQgUXrPgPn5oG6KFk2BF2hvqlaZh8I3',
#     client_secret='jqLjs9tEeSC41aiK'
# )

# try:
#     response = amadeus.reference_data.locations.points_of_interest.get(latitude=41.397158, longitude=2.160873)
#     print(response.data)
# except ResponseError as error:
#     print(error)

# TODO stick the api key in database, key broker, or encrypt to secure the key
API_KEY = 'AIzaSyD63DmxmF70vdriAA5zcmITd1dF2G7cD_o'
google_places = GooglePlaces(API_KEY)

place_result = google_places.nearby_search(location='London, England', 
keyword='Fish and Chips', radius=10, types=[types.TYPE_FOOD])

if place_result.has_attributions:
    print (place_result.html_attributions)

if place_result == 'OVER_QUERY_LIMIT':
    print("LALALALALALA")

for place in place_result:
    place.get_details()
    print(place.local_phone_number)
    print(place.details)
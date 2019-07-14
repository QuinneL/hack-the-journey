from amadeus import Client, ResponseError

amadeus = Client(
    client_id='CEQgUXrPgPn5oG6KFk2BF2hvqlaZh8I3',
    client_secret='jqLjs9tEeSC41aiK'
)

try:
    response = amadeus.reference_data.locations.points_of_interest.get(latitude=41.397158, longitude=2.160873)
    print(response.data)
except ResponseError as error:
    print(error)

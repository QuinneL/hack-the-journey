from amadeus import Client, ResponseError

amadeus = Client(
    client_id='CEQgUXrPgPn5oG6KFk2BF2hvqlaZh8I3',
    client_secret='jqLjs9tEeSC41aiK'
)

try:
    response = amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')
    print(response.data)
except ResponseError as error:
    print(error)

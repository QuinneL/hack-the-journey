from amadeus import Client, ResponseError

amadeus = Client(
    client_id='CEQgUXrPgPn5oG6KFk2BF2hvqlaZh8I3',
    client_secret='jqLjs9tEeSC41aiK'
)

#in real life the app would fetch information
profile_file = input('Name of profile json file')
trip_file = input('Name of trip json file')

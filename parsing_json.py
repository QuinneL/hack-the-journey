import json
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="TOTO")

class UserProfile:
    name = ""
    age = ""
    food = []
    drink = ""
    smoke = ""
    date = ""
    hobbies = []
    rest_or_play = ""
    wakeUp = ""
    sleep = ""

    def __init__(self, name, age, food, drink, smoke, date, hobbies, rest_or_play, wakeUp, sleep):
       self.name = name
       self.age = age
       self.food = food
       self.drink = drink
       self.smoke = smoke
       self.date = date
       self.hobbies = hobbies
       self.rest_or_play = rest_or_play
       self.wakeUp = wakeUp
       self.sleep = sleep

    '''
    checks if user is over 21
    returns: true if user is over 21 and false otherwise
    '''
    def is_over_21(self):
        return int(self.age) >= 21

    

'''
profile: JSON file for each USER made by the app
type: String
returns: UserProfile instance
'''
def parseProfile(profile):
    with open(profile) as json_file:
        profile_dict = json.loads(json_file.read())
        # creates an instance of a user with onboarding data stored
        user = UserProfile(profile_dict['name'], profile_dict['age'], 
        profile_dict['food'],profile_dict['drink'], profile_dict['smoke'], 
        profile_dict['date'], profile_dict['hobbies'], 
        profile_dict['rest_or_play'], profile_dict['wakeUp'], 
        profile_dict['sleep'])
        return user


class UserTrip:
    traveler_number = 1
    friends_family_romantic = "FAMILY"
    hotel_address = ""
    lat_long = (0,0)
    time_of_visit = []
    def __init__(self, traveler_number, who, hotel_address, time_of_visit):
       self.travelers = traveler_number
       self.friends_family_romantic = who
       self.hotel_address = hotel_address
       self.lat_long = (geolocator.geocode(hotel_address).latitude, geolocator.geocode(hotel_address).longitude)
       self.time_of_visit = time_of_visit


'''
usertrip: JSON file for each USER made by the app
type: String
returns: UserTrip instance
'''
def parseUserTrip(usertrip):
    with open(usertrip) as json_file:
        trip_dict = json.loads(json_file.read())
        user = UserTrip(trip_dict['travelers'], trip_dict['who'], trip_dict['hotel_address'], trip_dict['time_of_visit'])
        return user


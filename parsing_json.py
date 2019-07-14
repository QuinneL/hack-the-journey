import json

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
profile: json file for each USER made by the app
returns: maybe initialized global variables such as interests, sleep schedule
'''
def parseProfile(profile):
    with open(profile) as json_file:
        profile_dict = json.loads(json_file.read())
        user = UserProfile(profile_dict['name'], profile_dict['age'], 
        profile_dict['food'],profile_dict['drink'], profile_dict['smoke'], 
        profile_dict['date'], profile_dict['hobbies'], 
        profile_dict['rest_or_play'], profile_dict['wakeUp'], 
        profile_dict['sleep'])
        print(user.age)
        return user

'''
trip: json file for each trip made by the app
returns: maybe initialized global variables such as budget, dates, etc
'''
def parseTrip(trip):
    return 1


parseProfile('onboarding.json')
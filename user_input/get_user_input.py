import json
import os
import shutil


'''
prompts the user to answer profile questions
'''
def get_inputs():
  name = input("Name:")
  d = {}
  d['age'] = input("input your age and age of the people that you're traveling with:")
  d['date'] = input("Enter the range of date in YYYY-MM-DD, YYYY-MM-DD format:")
  d['hobbies'] = input("input your hobbies:")
  d['smoke'] = input("do you smoke? y or n")
  d['drink'] = input("do you drink? y or n")
  d['rest_or_play'] = input("do you like to rest or play?")
  d['favorite type of food']= input("your favorite type of food")
  d['budget'] = input("what is your budget for this trip?")
  d['sleep schedule'] =  input("what is your sleep schedule?")
  return(name, d)


def store_input():
  '''
  store user input into output
  '''
  output = {}
  while True:
    name, d = get_inputs()
    output[name] = d
    break

  '''
  creates a json file with user input
  '''
  with open('user_input.json','w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent=4)
  
  shutil.move('user_input.json', 'user_input/user_input.json')

if __name__ == '__main__':
  store_input()
"""
program to learn how dictionarys work
Created on 27.01.25

@author: paalhb
"""

    # dictionary

data = {
    "Norge": ["Oslo",0.634],
    "England": ["London",8.082],
    "Frankrike": ["Paris",2.161],
    "Italian": ["Roma",2.873]
}

    # variables

user_country = input("Hvilket land lurer du på? ")  # name of country

if user_country in data:  # check if country exist in dictionary and print
    capitol = data[user_country][0] # name of capitol
    citizens = data[user_country][1] # number of citizens
    print(f"Hovedstaden i {user_country} er {capitol}, og det er {citizens} mill. inbyggere i {capitol}.")
else:                                                                           
    print(f"{user_country} finnes ikke i listen.")
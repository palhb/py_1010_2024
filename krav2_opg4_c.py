"""
program to learn how to add data to a dictionary
Created on 27.01.25

@author: paalhb
"""

    # dictionary

data = {
    "Norge": ["Oslo",0.634],
    "England": ["London",8.082],
    "Frankrike": ["Paris",2.161],
    "Italia": ["Roma",2.873]
}

    # variables

user_country = input("Hvilket land har du info om? ")  # name of country

if user_country in data:  # check if country exist in dictionary and ask for inoput for new data
    print(f"{user_country} har vi allerede info om.")
else:
    capitol = input(f"Hva er hovedstaden i {user_country}? ")  # name of capitol
    citizens = input(f"Hvor mange millioner innbyggere bor det der? ")  # name of capitol
    data[user_country] = [capitol, citizens]
    print
    print(data)

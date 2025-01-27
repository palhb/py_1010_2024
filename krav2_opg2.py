"""
Calculation of numbers of pizza for a student porty
Created on 27.01.25

@author: paalhb
"""
import math

    # variables

students_count = int(input("Skriv inn antall elever: ")) # number of students coming to the party

pizza_count = math.ceil(students_count / 4) # calculation of number of whole pizzas needed to cover 1/4 pizza per student

print (f"\nDu må handle inn {pizza_count} pizzaer til festen") #

"""
Calulation of cost electric car vs gas car per year
Created on 06.11.24

@author: paalhb
"""

    # introduction

print(f"\nWelcome to Car Selector\nLet me help you decide on what type of car to buy:\n")
 
  # fixed cost variables 

cost_kwh = 2.00  # (cost in NOK per kwh)
cost_gas_km = 1.00  # (gas cost in NOK per km)
car_insurance_tax = 8.38 * 365  # (yearly cost to Statens Vegvesen)
km_per_year = 10000  # (yearly km usage)


  # fixed cost for car type
insurance_electric = 5000  # (insurance cost electric car in NOK)
insurance_gas = 7500  # (insurance cost gas car in NOK)
km_usage_cost_electric = ((0.2 * cost_kwh) * km_per_year)  # (kvW cost per year)
km_usage_cost_gas = (cost_gas_km * km_per_year)  # (kvW cost per year)
road_tax_electric = (0.1 * km_per_year)  # (road tax per year)
road_tax_gas = (0.3 * km_per_year)  # (road tax per year)


  # calculating total cost per year per car type

total_cost_electric_car = int (insurance_electric + car_insurance_tax + km_usage_cost_electric + road_tax_electric)
total_cost_gas_car = int (insurance_gas + car_insurance_tax + km_usage_cost_gas + road_tax_gas)

  # calculating price difference

most_expensive = max(total_cost_electric_car,total_cost_gas_car)

if most_expensive == total_cost_gas_car:
  price_difference = total_cost_gas_car - total_cost_electric_car
else:
    price_difference = total_cost_gas_car - total_cost_electric_car

  # calculated utput to console
print (f"Cost electric car per year: {total_cost_electric_car},- NOK")
print (f"Cost gas car per year: {total_cost_gas_car},- NOK")
print (f"\nThe cost is assuming you drive {km_per_year} km per year")
print (f"You can save {price_difference},- NOK per year by choosing the cheapest car type")

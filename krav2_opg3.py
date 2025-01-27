"""
Calculation of degrees to radians
Created on 27.01.25

@author: paalhb
"""
import numpy as np

    # variables

v_grad = float(input('Skriv inn gradtallet:' )) # float number for degrees

v_rad = v_grad*np.pi/180 # converstion from degrees to radians

print (f"\n {v_grad} grader, vil i radianer bli: {v_rad}  ")
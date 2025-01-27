"""
program to calculate areal and omkrets
Created on 27.01.25

@author: paalhb
"""

import numpy as np
import matplotlib.pyplot as plt

    # create function
def f(x):
    return -x**2 - 5

    # x variabel
x = np.linspace(-10, 10, 200)

    # y for x values
y = f(x)

    # plotting
plt.plot(x, y, label="f(x) = -x² - 5", color="blue", linewidth=2)

    # adding titles
plt.title("Graf av funksjonen f(x) = -x² - 5", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("f(x)", fontsize=14)

    # axlines
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.axvline(0, color="black", linestyle="--", linewidth=0.8)
plt.grid(True)

    # legend
plt.legend(fontsize=12)

    # show graph
plt.show()
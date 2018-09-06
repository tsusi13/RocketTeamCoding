"""
Air Speed Calculations for Ramjet Stabilization

Project: GW Rocket Team 2019 IREC/Capstone Project
Author: Thomas J Susi
Email: tsusi13@gwu.edu
Date: 2018-2019
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb

"""Gather Known Data from Excel"""

file = 'AirSpeedCalc.xlsx'

xl = pd.read_excel(file)

xlarray = xl.values

"""Array Data Place Markers"""
""" 0,1,2,3,4,5 = Time, Velocity, Acceleration, Altitude, Pressure, Density"""

"""Defining Functions"""

def massflowrate(density, area, velocity):

    massflowrate = density * area * velocity

    return massflowrate

"""User Input Intake Area"""

throat_area = float(input("Input Intake Area: "))

"""Solve for Mass Flow Curve"""

massflowdata = []
time = []

for n in range(0,2815):

    massflowdata.append(massflowrate(float(xlarray[n,5]), throat_area, float(xlarray[n,1])))
    time.append(float(xlarray[n,0]))

"""Plot Curve and Return it"""

plt.plot(time, massflowdata)
plt.grid(True)
plt.xlabel('Time (Seconds)')
plt.ylabel('Mass Flow Rate (kg/s)')
plt.title('Mass Flow Rate through Ram Inlet')
plt.show()

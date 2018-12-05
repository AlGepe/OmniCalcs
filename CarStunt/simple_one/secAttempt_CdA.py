##### Most simple approach:
        # Point-like car
        # constant air resistance (using CdA of the car and takeoff speed)

## 53kph for a 20 long jump seems too slow to make it...
import numpy as np
from matplotlib import pyplot as plt


'''
theta_deg = float(input("Angle of the take off ramp [in degrees]"))
hr = float(input("Height of the takeoff ramp wrt the ground [in m]"))
H = float(input("Height of the landing wrt the ground [in m]"))
L = float(input("Distance between the takeoff ramp and the landing [in m]"))
CdA = float(input("CdA value of the car jumping [in m^2]"))
rho = float(input("Air density [in kg/m^3]"))
m = float(input("Mass of the car [in kg]"))
'''

theta_deg = 45.
hr = 0.
H = 2.
L = 20.
CdA = .76
rho = 1.225
m = 1500
# v_kph = float(input("Speed of the car at the moment of takeoff [in km/h]"))
g = 9.8 # m/s*s


# Convert to SI and useful values
thetaRad = (theta_deg/360.)* 2 * np.pi
# v_ms = v_kph * 1000 / 3600.
hl = H - hr

cosT = np.cos(thetaRad)
cosT2 = cosT * cosT
R = (-rho * CdA * cosT2)/m

P = 2*(-cosT - np.sqrt(cosT2 + (R * L))/(R))
P = 2*(-cosT + np.sqrt(cosT2 + (R * L))/(R))
print(P)
v_min = np.sqrt((g*P*P)/(2*(np.sin(thetaRad) * P - hl)))

print("Take off speed")
print(str(v_min * 3.6) + " km/h")

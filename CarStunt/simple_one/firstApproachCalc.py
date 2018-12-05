##### Most simple approach:
        # Point-like car
        # No friction

## 53kph for a 20 long jump seems too slow to make it...
import numpy as np
from matplotlib import pyplot as plt


theta_deg = float(input("Angle of the take off ramp [in degrees]"))
hr = float(input("Height of the takeoff ramp wrt the ground [in m]"))
H = float(input("Height of the landing wrt the ground [in m]"))
L = float(input("Distance between the takeoff ramp and the landing [in m]"))
# v_kph = float(input("Speed of the car at the moment of takeoff [in km/h]"))
g = 9.8 # m/s*s


# Convert to SI and useful values
thetaRad = (theta_deg/360.)* 2 * np.pi
# v_ms = v_kph * 1000 / 3600.
he = H - hr

v_min = (L/np.cos(thetaRad)) * np.sqrt(np.abs(g)/(2*(L*np.tan(thetaRad) - he)))

print(str(v_min * 3.6) + 'km/h')

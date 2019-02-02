'''This code is used to compare the coulombic force and elastic interaction force.'''

import numpy as np

linecommon = "========================================================\n"
mu   = 116.5*10**(9)
nu   = 0.18
bmag = 4.218/np.sqrt(2)*10**(-10)
h    = 0.5*bmag

e    = 1.602176634*10**(-19)
q1   = 1.0*e
epsilon_0 = 8.8542*10**(-12)  # unit C^2/(N*m^2)
epsilon_r = 7.3665
epsilon   = epsilon_0 * epsilon_r

f_elastic = mu*bmag**2*h**2/(8*np.pi*(1-nu))
f_coulomb = q1**2/(4*np.pi*epsilon)

print("f_elastic = %25.16e " %f_elastic)
print("f_coulomb = %25.16e " %f_coulomb)
print(linecommon)

if(f_coulomb > f_elastic):
    print("The electrostatic force is dominant.")
else:
    print("The elastic force is dominant.")
'''This code is used to compare the coulombic force and elastic interaction force.'''
'''Shear modulus, poisson ratio and dielectric constant are calculed by GULP.'''

import numpy as np

linecommon = "===========================================================\n"
pressure   = input("Please specify pressure of system : 100, 60, 30 or 0 (unit in GPa) \n")
if(pressure == '100'):
    alat =  3.828
    mu   =  204.44991
    nu   =  0.26630
    epsilon_r = 4.89905
elif(pressure == '60'):
    alat =  3.9355
    mu   =  182.26174
    nu   =  0.27421
    epsilon_r = 5.63823
elif(pressure == '30'):
    alat =  4.047
    mu   =  162.31686
    nu   =  0.28573
    epsilon_r = 6.69607
elif(pressure == '0'):
    alat =  4.218
    mu   =  137.46615
    nu   =  0.31095
    epsilon_r = 9.29388
else:
    print("The pressure is not included in the code.")
    alat = float(input("Please give lattice parameter: \n"))
    mu   = float(input("Please give  shear   modulus : \n"))
    nu   = float(input("Please give  poisson  ratio  : \n"))
mu   = mu * 10**9                 # change GPa to Pa
bmag = alat/np.sqrt(2)*10**(-10)  # change Angestrm to m
h    = 0.5*bmag                   # Height of jog

e    = 1.602176634*10**(-19)
q1   = 1.0*e
epsilon_0 = 8.8542*10**(-12)  # unit C^2/(N*m^2)
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
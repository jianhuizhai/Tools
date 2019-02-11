'''This code is used to calculate jog elastic interaction energy'''
'''mu and nu are shear modulus and poisson ration, respectively. isotropic is considered.'''
'''mu and nu are calculated by GULP.'''

import numpy as np


linecommon = "=======================================================================================\n"
#=======================================================================================
#                      specify slip system
#=======================================================================================
slip_system = input("Slip system : 110  <------>   001 \n")

if(slip_system != '110' and slip_system !='001'):
    print("The slip system is not included in this code.")
    exit()
print(linecommon)

#=======================================================================================
#                        material parameter under different pressures
#=======================================================================================
pressure = int(input("type the pressure of system: (100, 60, 30 or 0 -- units in GPa)"+"\n"))

if(pressure == 100):
    alat = 3.82776
    mu   =  204.44991
    nu   =  0.26630
elif(pressure == 60):
    alat = 3.9355
    mu   =  182.26174
    nu   =  0.27421
elif(pressure == 30):
    alat = 4.047
    mu   =  162.31686
    nu   =  0.28573
elif(pressure == 0):
    alat = 4.218
    mu   =  137.46615
    nu   =  0.31095
else:
    print("The pressure is not included in the code.")
    exit()

print(linecommon)
#=======================================================================================
#                               jog geometry
#=======================================================================================
h = float(input("The height of jog (units: atom spacing) \n"))
w = float(input("The width of jog pair: (units: Angstrom) \n"))

bmag        = alat/np.sqrt(2)  # Angstrom
if(slip_system == '110'):
    atom_space  = 0.5*bmag
else:
    atom_space  = 0.5*alat

print('mu               : ', mu,  '     nu   = ', nu) 
print('lattice constant : ', alat,'     bmag = ', bmag)
print(linecommon)
#=======================================================================================
#                       calculate elastic interaction energy
#=======================================================================================
Eint = -mu*bmag**2*(h*atom_space)**2/(8*np.pi*w*(1-nu))
Eint = Eint/160.21766208

print("The elastic energy of unit  height jog under PBC is : ", np.log(4)*Eint)
print("The elastic energy of twice height jog under PBC is : ", 2*np.log(4)*Eint)
print(linecommon)
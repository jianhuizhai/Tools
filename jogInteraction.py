'''This code is used to calculate jog elastic interaction energy'''
'''mu and nu are shear modulus and poisson ration, respectively. anisotropic is considered.'''

import numpy as np


linecommon = "=======================================================================================\n"
#=======================================================================================
#                             calculation choice
#=======================================================================================
interaction_flag = input("Do you want to calculate elastic interaction energy: y or n \n")

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
    mu   = 294.3
    if(slip_system == '110'):
        nu   = 0.27
    elif(slip_system == '001'):
        nu   = 0.16
elif(pressure == 60):
    alat = 3.9355
    mu   = 236.7
    if(slip_system == '110'):
        nu   = 0.25
    elif(slip_system == '001'):
        nu   = 0.18
elif(pressure == 30):
    alat = 4.047
    mu   = 184.4
    if(slip_system == '110'):
        nu   = 0.23
    elif(slip_system == '001'):
        nu   = 0.20
elif(pressure == 0):
    alat = 4.218
    mu   = 116.5
    if(slip_system =='110'):
        nu   = 0.18
    elif(slip_system == '001'):
        nu   = 0.27
else:
    print("The pressure is not included in the code.")
    exit()

eV2GPa = 160.21766208

print(linecommon)



#=======================================================================================
#                           estimate  jog formation energy
#=======================================================================================
bmag = alat/np.sqrt(2)  # Angstrom
h    = float(input("The height of jog (units: atom spacing) \n"))

if(slip_system == '110'):
    atom_space  = 0.5*bmag
else:
    atom_space  = 0.5*alat

h     = h*atom_space

W_f = 0.25*mu*bmag**2*h/(np.pi * (1-nu))
print('mu               : ', mu,  '     nu   = ', nu) 
print('lattice constant : ', alat,'     bmag = ', bmag)
print('Formation energy : ', W_f/eV2GPa)
print(linecommon)
#=======================================================================================
#                               jog interaction
#=======================================================================================
if( interaction_flag == 'y'):
    w = float(input("The width of jog pair: (units: Angstrom) \n"))

    #=======================================================================================
    #                       calculate elastic interaction energy
    #=======================================================================================
    Eint = -mu*bmag**2*h*2/(8*np.pi*w*(1-nu))
    Eint = Eint/eV2GPa

    print("The elastic energy under periodic boundary condition : ", np.log(4)*Eint)
    print("This is the energy just for one jog pair. <===Attention !!!!!!")
    print(linecommon)
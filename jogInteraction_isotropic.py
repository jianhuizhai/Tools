'''This code is used to calculate jog elastic interaction energy'''
'''mu and nu are shear modulus and poisson ration, respectively. isotropic is considered.'''
'''mu and nu are calculated by GULP.'''

import numpy as np


linecommon_major = "=======================================================================================\n"
linecommon_minor = "---------------------------------------------------------------------------------------\n"
#=======================================================================================
#                      specify slip system
#=======================================================================================
slip_system = input("Slip system : 110  <------>   001 \n")

if(slip_system != '110' and slip_system !='001'):
    print("The slip system is not included in this code.")
    exit()
print(linecommon_major)

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

eV2GPa = 160.21766208
print(linecommon_major)
#=======================================================================================
#                               jog geometry
#=======================================================================================
bmag = alat/np.sqrt(2)  # Angstrom
print('mu               : ', mu,  '     nu   = ', nu) 
print('lattice constant : ', alat,'     bmag = ', bmag, '\n')

if(slip_system == '110'):
    atom_space  = 0.5*bmag
else:
    atom_space  = 0.5*alat

box_size, width = np.loadtxt('width_jog_'+slip_system+'_'+str(pressure)+'GPa.dat', unpack=True)

for i in range(len(box_size)):
    w = width[i]
    print("                     The box size is %10i " %box_size[i])
    print(linecommon_major)
    for h in (1,2):
        if(h==1):
            jog_type = 'unit jog'
        elif(h==2):
            jog_type = 'twice jog'
        else:
            print("Unkown jog type! Please check the code!")
        print('h = ', h)
        height = h*atom_space

        W_f = 0.25*mu*bmag**2*height/(np.pi * (1-nu))

        print(linecommon_minor)
    #=======================================================================================
    #                               jog interaction
    #=======================================================================================
    

    #=======================================================================================
    #                       calculate elastic interaction energy
    #=======================================================================================
        Eint = -mu*bmag**2*height**2/(8*np.pi*w*(1-nu))
        Eint = Eint/eV2GPa

        print('The formation and elastic interaction energy of %s are: ' %jog_type)
        print(linecommon_minor)
        print('Formation energy : ', W_f/eV2GPa)
        print("The elastic energy of one jog pair under periodic boundary condition : ", np.log(4)*Eint)
        print("The elastic energy of two jog pair under periodic boundary condition : ", 2*np.log(4)*Eint)
        print(linecommon_minor)
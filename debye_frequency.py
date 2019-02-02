# Debye temperature is taken from paper: 
# Melting temperatures of MgO under high pressure by micro-texture analysis

import numpy as np

debye_temp = 936                    
h          = 6.62607015*10**-34
k_b        = 1.380649*10**-23

freq       = k_b*debye_temp/h

print('Debye frequence of MgO is %10.9e' %freq)

a = 4.218e-10  # lattice parameter in meter
f = 0.7815
D_sd = f*a**2*freq*np.exp(4.1/2)     # This is D0, preexponential parameter; f is correlation factor
print('Self diffusion coefficient of MgO is %10.9e' %D_sd)
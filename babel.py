import numpy as np
import os
import linecache
import sys

img = int(input("How mangy replicas? \n"))
#=============================================================================
linecommon = '===============================================================\n'
Correction = open('nebpath_correction.dat', 'w')
#=============================================================================
#             run specified input file in specified folder
#=============================================================================
energy1 = np.zeros(img); energy2 = np.zeros(img)
energy = np.zeros(img)
de     = np.zeros(img)

for i in range(img):
    print(linecommon)
    os.chdir('img'+str(i+1))
    print("cwd:    ", os.getcwd())
    babel = os.system('babel input_dislo.babel >output_dislo.babel')
    line1 = linecache.getline(os.path.abspath('output_dislo.babel'), 122)
    line2 = linecache.getline(os.path.abspath('output_dislo.babel'), 128)
    #print(os.path.abspath(filename))
    energy1[i] = line1.split()[13]
    print('energy1 = ', energy1[i])
    energy2[i] = line2.split()[6]
    energy[i]  = energy1[i] + energy2[i]

    de[i] = energy[i] - energy[0]
    print("energy[i] = ", energy[i], "energy[0] = ", energy[0])
    print(de[i])
    os.chdir("../")
    line = '%-2i %16.8f \n' %(i+1, de[i])
    Correction.write(line)
Correction.close
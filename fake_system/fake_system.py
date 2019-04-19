"""
This code is used to visulization of energy by using dumpfile.
The energy value of deleted atoms are assigned to 5.
The energy value of not considered atoms are assigned to 20.
"""
import numpy as np
import sys
import linecache
from output_fake import DumpOutput

linecommon = '========================================================='

print(linecommon)
n = int(input("How many atoms are deleted : "))
ions=[]
while (n>0):
    ions.append(input("atom id : "))
    n = n-1

ions = np.array( ions, dtype = int )  # change list to int array. 
print(ions)


lmp_file    = sys.argv[1]
energy_file = sys.argv[2]

print(linecommon)
print("lmp_file    : ", lmp_file)
print("energy_file : ", energy_file)
print(linecommon)

xlim = linecache.getline(lmp_file, 6)
ylim = linecache.getline(lmp_file, 7)
zlim = linecache.getline(lmp_file, 8)

print(xlim, end='')
print(ylim, end='')
print(zlim, end='')
print(linecommon)

skipline  = 16
atom_id, atom_type, x,y,z = np.loadtxt(lmp_file, skiprows=skipline, usecols=(0,1,2,3,4), unpack=True)
eng_id, eng_eng = np.loadtxt(energy_file, usecols=(0,5), unpack=True)

'''
print("type(atom_id) : ", type(atom_id))
print("type(ions) : ", type(ions))
'''

Eng = np.ones(len(atom_id))*20
#print("Eng", Eng)


for i in range(len(atom_id)):
    for k in range(len(ions)):
        if(atom_id[i] == ions[k]):
            Eng[i] = 5
    for j in range(len(eng_id)):
        if( atom_id[i] == eng_id[j] ):
            Eng[i] = eng_eng[j]

DumpOutput('dump.eng',xlim, ylim, zlim, atom_id, atom_type, x, y, z, Eng)
print("Output file: dump.eng")
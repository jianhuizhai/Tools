import numpy as np
import sys
import linecache
from output_fake import DumpOutput

linecommon = '========================================================='

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

Eng = np.zeros(len(atom_id))

#print("Eng", Eng)

for i in range(len(atom_id)):
    for j in range(len(eng_id)):
        if( atom_id[i] == eng_id[j] ):
            Eng[i] = eng_eng[j]
            break
        else:
            Eng[i] = 20

DumpOutput('dump.eng',xlim, ylim, zlim, atom_id, atom_type, x, y, z, Eng)
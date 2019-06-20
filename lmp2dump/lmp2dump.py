#! /usr/bin/python3

import os
import numpy as np
import linecache
from output import DumpOutput

linecomment = '='*80

dumpfile = 'dump.relax0'
if os.path.exists( dumpfile ):
    exit('{} exists.'.format( dumpfile ) )

lmp_file = 'initial.lmp'

if not os.path.exists( lmp_file ):
    os.system('bash build_noclimb.sh')

xlim = linecache.getline(lmp_file, 6)
ylim = linecache.getline(lmp_file, 7)
zlim = linecache.getline(lmp_file, 8)

print( linecomment )
print(xlim, end='')
print(ylim, end='')
print(zlim, end='')

atom_id, atom_type, charge, x, y, z = np.loadtxt( lmp_file, skiprows=16, usecols=([0,1,2,3,4,5]), unpack=True)

DumpOutput( dumpfile, xlim, ylim, zlim, atom_id, atom_type, x, y, z)

print('{} successfully generated.'.format( dumpfile ) )
#! /usr/bin/python3

import os
import numpy as np

linecommon = '='*80

folders, binding_energy = np.loadtxt('energy_info.dat', usecols=([0,6]), unpack=True )
keepFolder=[]
#if flag_keep == '1' :
for i in range( len(folders) ):
    if binding_energy[i] <= 0 :
        keepFolder.append( folders[i] )

for folder in os.listdir('.'):
    if os.path.isdir(folder):
        if any( [ folder == str( int(k) ) for k in keepFolder ] ):
            print(linecommon)
            print( "generate dump.relax0 in folder : {:10s}".format(folder) )
                
            os.chdir( folder )
            os.system('python ~/bin/lmp2dump.py')
            os.chdir( '../' )
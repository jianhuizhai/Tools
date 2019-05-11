import numpy as np
import os

linecommon = "==============================================================================================="

folders = np.loadtxt('energy_info.dat', dtype=str,usecols=(0))
keepFolder = folders[0]
print(keepFolder, type(keepFolder) )

for folder in os.listdir('.'):
    if os.path.isdir(folder):
        if folder == keepFolder:
            print(linecommon)
            print( "{}{:10s}".format('The dumpfiles in this folder are keeped.  ',   folder) )
        
        elif folder != 'reference' and folder != '__pycache__' :
            print(linecommon)
            print(folder)
            os.chdir( folder )
            print('deleting dumpfiles in this folder')
            os.system('rm -f dump.relax*')
            os.system('rm -f *.out')
            os.chdir('../')
            

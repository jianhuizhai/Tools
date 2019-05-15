#! /usr/bin/python3

import numpy as np
import os

linecommon = "==============================================================================================="

print( linecommon )
flag = input("delete just subfolders (1) or walk through subfolders (2) : ")
print( linecommon )

if flag == '1':
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

elif flag == '2' :
    path = os.getcwd()
    print( 'current folder : \n', path )
    for folderName, subfolders, filenames in os.walk( path ):
        for subfolder in subfolders:
            if subfolder == 'v_mg' or subfolder == 'v_o':
                energy_infoPath = os.path.join(path, folderName, subfolder )
                if os.path.exists( os.path.join(energy_infoPath, 'energy_info.dat') ):
                    print( linecommon )
                    print( energy_infoPath )
                    energy_infoFolders = np.loadtxt(os.path.join(energy_infoPath, 'energy_info.dat'), dtype= int ,usecols=([0]) ) 
                    keepFolder         = str( energy_infoFolders[0] )
                    for folder in os.listdir( energy_infoPath ):
                        #print('things in %s : %s' %(energy_infoPath,folder) )
                        if os.path.isdir( os.path.join(energy_infoPath,folder) ):  # import. It will only show part of folders in this folder is use os.path.isdir(folder)
                            #print( linecommon )
                            #print('folder in %s : %s' %(energy_infoPath, folder) )  
                            if folder == keepFolder:
                                print(linecommon)
                                print( "{}{:10s}".format('The dumpfiles in this folder are keeped.  ',   folder) )
        
                            elif folder != 'reference' and folder != '__pycache__' :
                                print(linecommon)
                                print('deleteing dumpfiles in folder : %10s' %folder )
                                for filename in os.listdir( os.path.join(energy_infoPath, folder) ):
                                    if filename.startswith('dump.relax'):
                                        print( filename )
                                        os.remove( os.path.join(energy_infoPath, folder, filename) )  ## this line should be uncommented when using this code to delete files
                            
                else:
                    print( linecommon )
                    exit('energy_info doesn\'t exists in %s' %energy_infoPath )

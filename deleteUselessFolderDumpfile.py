#! /usr/bin/python3

import numpy as np
import os

linecommon = "==============================================================================================="

print( linecommon )
flag = input("delete just subfolders (1) or walk through subfolders (2) : ")
flag_info = input("Do you want to show the info about deleted files (y or n) : ")
print( linecommon )

if flag == '1':
    folders = np.loadtxt('energy_info.dat', dtype=str,usecols=(0))
    keepFolder = folders[0]
    # print(keepFolder, type(keepFolder) )
    for folder in os.listdir('.'):
        if os.path.isdir(folder):
            if folder == keepFolder:
                print(linecommon)
                print( "{}{:10s}".format('The dumpfiles in this folder are keeped.  ',   folder) )
        
            elif folder != 'reference' and folder != '__pycache__' :
                if flag_info == 'y':
                    print(linecommon)
                    print('deleting dumpfiles in folder : %10s.' %folder)
                os.chdir( folder )
                os.system('rm -f dump.relax*')
                os.system('rm -f *.lmp *.out')
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
                                if flag_info == 'y' :
                                    print(linecommon)
                                    print( "{}{:10s}".format('The dumpfiles in this folder are keeped.  ',   folder) )

                            # delete files in folder : reference
                            elif folder == 'reference' :
                                # keep the last dump file in order to have a look at config
                                if flag_info == 'y' :
                                    print( linecommon )
                                    print( 'deleting files in folder : reference')
                                for filename in os.listdir( os.path.join(energy_infoPath, folder) ):
                                    if filename.endswith('.lmp') or filename == 'dump.relax0':
                                        if flag_info == 'y':
                                            print( filename )
                                        os.remove( os.path.join(energy_infoPath, folder, filename) )
                            
                            # delete files in other folders
                            else:
                                if flag_info == 'y':
                                    print(linecommon)
                                    print('deleteing dumpfiles in folder : %10s' %folder )
                                
                                
                                for filename in os.listdir( os.path.join(energy_infoPath, folder) ):
                                    if filename.startswith('dump.relax'):
                                        if flag_info == 'y':
                                            print( filename )
                                        os.remove( os.path.join(energy_infoPath, folder, filename) )
                                    
                                    if filename.startswith('slurm'):
                                        if flag_info == 'y':
                                            print( filename )
                                        os.remove( os.path.join(energy_infoPath, folder, filename) )
                                    
                                    # delete .lmp file in the folder
                                    if filename.endswith('.lmp') :
                                        if flag_info == 'y':
                                            print( filename )
                                        os.remove( os.path.join(energy_infoPath, folder, filename) )
                                
                else:
                    print( linecommon )
                    exit('energy_info doesn\'t exists in %s' %energy_infoPath )
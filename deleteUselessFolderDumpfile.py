#! /usr/bin/python3

import numpy as np
import os

linecommon = "="*100

print( linecommon )
flag      = input("delete just subfolders (1) or walk through subfolders (2) : ").lower()
flag_lmp  = input("Do you want to delete lmp file : ").lower()
flag_info = input("Do you want to show the info about deleted files (y or n) : ").lower()
flag_keep = input("Do you want to keep the negative binding energy (1) or just the most favorable one (2) (1 or 2) : ")
print( linecommon )

if flag == '1':
    folders, binding_energy = np.loadtxt('energy_info.dat', usecols=([0,6]), unpack=True )
    keepFolder=[]
    if flag_keep == '1' :
        for i in range( len(folders) ):
            if binding_energy[i] <= 0 :
                keepFolder.append( folders[i] )
    elif flag_keep == '2':
        for i in range(3):
            keepFolder.append( folders[i] )
    '''
    for k in keepFolder:
        print( 'keepFolder :', k )
    # print(keepFolder, type(keepFolder) )
    '''
    for folder in os.listdir('.'):
        if os.path.isdir(folder):
            if any( [ folder == str( int(k) ) for k in keepFolder ] ):
                print(linecommon)
                print( "The dumpfiles in this folder are keeped : {:10s}".format(folder) )
                
                os.chdir( folder )
                os.system('rm -f dump.relax0 slurm*')
                if flag_lmp == 'y':
                    os.system( 'rm -f *.lmp' )
                os.chdir( '../' )
        
            elif folder != 'reference' and folder != '__pycache__' :
                if flag_info == 'y':
                    print(linecommon)
                    print('deleting dumpfiles in folder : %10s.' %folder)
                os.chdir( folder )
                os.system('rm -f dump.relax* slurm*')
                if flag_lmp == 'y':
                    os.system('rm -f *.lmp ')
                os.chdir('../')
            elif folder == 'reference':
                if flag_info == 'y':
                    print(linecommon)
                    print('deleting files in folder : {:10s}'.format(folder) )
                os.chdir( folder )
                os.system( 'rm -f dump.relax0 slurm*' )
                if flag_lmp == 'y':
                    os.system( 'rm -f *.lmp ' )
                os.chdir('../')

elif flag == '2' :
    path = os.getcwd()
    print( 'current folder : \n', path )
    for folderName, subfolders, filenames in os.walk( path ):
        for subfolder in subfolders:
            if subfolder == 'v_mg' or subfolder == 'v_o':
                energy_infoPath = os.path.join(path, folderName, subfolder )
                
                if not os.path.exists( os.path.join(energy_infoPath, 'energy_info.dat') ):
                    ## obtain energy_info.dat
                    os.system('python ~/bin/extractData_binding_energy.py')
                
                else :
                    print( linecommon )
                    print( energy_infoPath )
                
                    # determine folders are keeped
                    folders, binding_energy = np.loadtxt( os.path.join(energy_infoPath, 'energy_info.dat'), usecols=([0,6]), unpack=True )
                    
                    keepFolder=[]
                    if flag_keep == '1' :
                        for i in range( len(folders) ):
                            if binding_energy[i] <= 0 :
                                keepFolder.append( folders[i] )
                    elif flag_keep == '2':
                        for i in range(3):
                            keepFolder.append( folders[i] )

                    for folder in os.listdir( energy_infoPath ):
                        if os.path.isdir( os.path.join(energy_infoPath,folder) ):  # import. It will only show part of folders in this folder is use os.path.isdir(folder)
                            if any( [ folder == str( int(k) ) for k in keepFolder ] ) :
                                if flag_info == 'y' :
                                    print(linecommon)
                                    print( "The dumpfiles in this folder are keeped : {:10s}".format(folder) )
                                os.chdir( folder )
                                os.system('rm -f dump.relax0 slurm*')
                                if flag_lmp == 'y':
                                    os.system( 'rm -f *.lmp' )
                                os.chdir( '../' )

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
                                    if filename.startswith('slurm'):
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
                                    
                                    if filename.endswith('.lmp') and flag_lmp=='y' :
                                        if flag_info == 'y':
                                            print( filename )
                                        os.remove( os.path.join(energy_infoPath, folder, filename) )

#! /usr/bin/python3

import os
import zipfile
import time
import numpy as np

linecommont = '='*80

print( linecommont )
flag     = input(""">>>>>>>>>   just subfolders --- 1 
>>>>>>>>>   walk through subfolders --- 2 
>>>>>>>>>   1 or 2 : """)

print( linecommont )
flag_zip = input('''>>>>>>>>>   zip --- 1
>>>>>>>>>   unzip --- 2
>>>>>>>>>   1 or 2 : ''')
print(linecommont)

zip_filename = 'results.zip'

if flag_zip == '2' :
    flag_rm = input('''Do you want to remove {} (y or n) : '''.format(zip_filename) ).lower()

begin = time.time()



if flag == '1':

    for folder in os.listdir('.'):
        if os.path.isdir( folder ) :
            print( linecommont )
            print( 'folder : {}'.format( folder ) )
            os.chdir( folder )
            #os.system('rm -r home')
            # zip all folders
            if flag_zip == '1' :
                if os.path.exists( zip_filename ):
                    print('{} exists.'.format( zip_filename ) )
                else:
                    print('zip files : ' )
                    with zipfile.ZipFile('results.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip:
                        for filename in os.listdir('.'):
                            if filename.endswith('lmp') or filename.endswith('.sh'):
                                zip.write( filename )
                                os.remove( filename )
                            if filename == 'log.lammps':
                                zip.write( filename )
                            if filename.startswith('dump.relax'):
                                zip.write( filename )
                                os.remove( filename )
                    #print( zip.namelist() )
            
            # unzip
            elif flag_zip == '2':
                # unzip
                if not os.path.exists( zip_filename ):
                    print('{} does not exist.'.format( zip_filename ) )
                
                # only unzip results.zip in keepFolders which binding energy is negative
                # vacancy is favorable to bind to the positive instead of staying in buck
                else :
                    with zipfile.ZipFile('results.zip', 'r') as zip :
                        print('unzip files : \n{}'.format( zip.namelist() ) )
                        zip.extractall(path='.')
                
                    if flag_rm == 'y' :
                        os.remove( zip_filename )
                
            os.chdir('../')


elif flag == '2' :
    path = os.getcwd()
    print( 'current folder : \n', path )
    
    for folderName, subfolders, filenames in os.walk( path ):
        workPath = os.path.join( path, folderName)
        os.chdir( workPath )
        print( 'folder : {}'.format( workPath ) )
        # zip all folders
        if flag_zip == '1' :
            if os.path.exists( zip_filename ):
                print('{} exists.'.format( zip_filename ) )
            else:
                with zipfile.ZipFile( 'results.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip:
                    for filename in os.listdir( '.' ):
                        if filename.endswith('lmp') or filename.endswith('.sh'):
                            zip.write( filename )
                            os.remove( filename )
                        if filename == 'log.lammps':
                            zip.write( filename )
                        if filename.startswith('dump.relax'):
                            zip.write( filename )
                            os.remove( filename )
                        if filename.startswith('slurm'):
                            os.remove( filename )
            #print( zip.namelist() )
        # unzip
        elif flag_zip == '2' :
            if not os.path.exists( zip_filename ):
                print('{} does not exists.'.format( zip_filename ) )
                            
            else :
                with zipfile.ZipFile('results.zip', 'r') as zip :
                    zip.extractall(path='.')
                if flag_rm == 'y' :
                    os.remove( zip_filename )
        os.chdir(path)

if flag_zip == '1':
    print('zip files')
else:
    print('unzip files.')
end = time.time()
print( linecommont )
print('running time is : {:10.2f} mins '.format( (end-begin)/60. ) )
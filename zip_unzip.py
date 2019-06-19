#! /usr/bin/python3

import os
import zipfile
import time

linecommont = '='*80

print( linecommont )
flag     = input(""">>>>>>>>>   just subfolders --- 1 
>>>>>>>>>   walk through subfolders --- 2 
>>>>>>>>>   1 or 2 : """).lower()

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
        if os.path.isdir( folder ):
            print( linecommont )
            print( 'folder : {}'.format( folder ) )
            os.chdir( folder )
            #os.system('rm -r home')
            # zip
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
                                os.remove( filename ) 
                            if filename.startswith('dump.relax'):
                                zip.write( filename )
                                os.remove( filename )
                    #print( zip.namelist() )
            
            # unzip
            elif flag_zip == '2':
                # unzip
                if not os.path.exists( zip_filename ):
                    exit('{} does not exist.'.format( zip_filename ) )
                with zipfile.ZipFile('results.zip', 'r') as zip :
                    print('unzip files : {}'.format( zip.namelist() ) )
                    zip.extractall(path='.')
                
                if flag_rm == 'y' :
                    os.remove( zip_filename )
                
            os.chdir('../')


elif flag == '2' :
    path = os.getcwd()
    print( 'current folder : \n', path )
    
    for folderName, subfolders, filenames in os.walk( path ):
        for subfolder in subfolders:
            if subfolder == 'v_mg' or subfolder == 'v_o':
                energy_infoPath = os.path.join(path, folderName, subfolder )
                print( linecommont )
                print( 'subfolder : {} '.format(energy_infoPath) )

                for folder in os.listdir( energy_infoPath ) :
                    if os.path.isdir( os.path.join(energy_infoPath,folder) ):
                        os.chdir( os.path.join( energy_infoPath, folder) )
                        print( 'folder : {}'.format( folder ) )
                        # zip
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
                                            os.remove( filename )
                                        if filename.startswith('dump.relax'):
                                            zip.write( filename )
                                            os.remove( filename )
                                        if filename.startswith('slurm'):
                                            os.remove( filename )
                                #print( zip.namelist() )
                        # unzip
                        elif flag_zip == '2' :
                            
                            with zipfile.ZipFile('results.zip', 'r') as zip :
                                zip.extractall(path='.')
                            if flag_rm == 'y' :
                                os.remove( zip_filename )
    os.chdir(path)

end = time.time()
print( linecommont )
print('running time is : {}s'.format(end-begin) )
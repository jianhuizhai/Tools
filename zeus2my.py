import os
import numpy as np
linecomment = '='*80

#================================================================================================
#                       check energy_info.dat exists or not
#================================================================================================

flag_cp     = input("Do you want to copy things to zeus (1) or to your computer (2)--- (1 or 2) : ")

if not os.path.exists('energy_info.dat'):
    print( linecomment )
    flag = input('energy_info.dat does not exists. Do you want to continue (y or n) ? : ').lower()
    if flag =='y':
        leaveFolder = input("give the folder that things are not copy : ")
    else:
        exit('exit the code.')
else:
    leaveFolders = np.loadtxt('energy_info.dat',usecols=([0]))

#================================================================================================
#               determine the work direction in zeus
#================================================================================================

workDirectionZeus = os.getcwd()[50:]
zeuspre = 'jianhui.zhai@zeus.univ-lille.fr:/home/jianhui.zhai/edge_110/100x101/'
workDirectionZeus = zeuspre + workDirectionZeus
print( linecomment )
print(workDirectionZeus)

#================================================================================================
#                   cp runned.dat to zeus
#================================================================================================
if flag_cp == '1' :
    os.system('scp *.dat {}'.format(workDirectionZeus) )
elif flag_cp == '2':
    os.system('scp {}/*.dat .'.format(workDirectionZeus) )
#================================================================================================
#                   cp folder in zeus to my work direction
#================================================================================================
count = 0

'''
for folder in os.listdir('.'):
    if os.path.isdir( folder ) and not any( [folder == str(int(leaveFolder)) for leaveFolder in leaveFolders ] ) :
        print( folder )

for leaveFolder in leaveFolders:
    print( int(leaveFolder) )
print(len(leaveFolders))
'''

for folder in os.listdir('.'):
    if os.path.isdir( folder ) and not any( [folder == str(int(leaveFolder)) for leaveFolder in leaveFolders ] ) :
        if flag_cp == '1' :   # to zeus
            #print('scp -r {} {}'.format(folder, workDirectionZeus) )
            print( '='* 80 )
            print(f'copying folder : {folder:s}')
            #os.chdir( folder )
            #os.system('scp * {}/{}'.format( workDirectionZeus, folder) )
            print( 'scp -r {1}/ {0}'.format( workDirectionZeus, folder) )
            os.system( 'scp -r {1}/ {0}'.format( workDirectionZeus, folder) )
            #os.chdir('../')
                    
            count += 1
            
        if flag_cp == '2' and [folder != str(int(leaveFolder) ) for leaveFolder in leaveFolders ] :  # to my computer
            #print('scp -r {}/{} .'.format(workDirectionZeus,folder) )
            print( '=' * 80 )
            print(f'copying folder : {folder:s}')
            os.chdir( folder )
            os.system('scp {}/{}/* .'.format(workDirectionZeus, folder) )
            os.chdir('../')
            
            count += 1

print( linecomment )
print('count = {}'.format(count) )
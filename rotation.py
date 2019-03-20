'''This file is used to rotate the atoms along x axis by a specified degree from a xyz data file.'''
'''After rotate, dump atoms which can be opened by OVITO software.'''
'''The info of xyz data file is : atom id, x, y, z, element'''

import numpy as np
import sys
import string

#===============================================================================================
common   = '======================================================================\n'

#===============================================================================================
#               define dump function
#===============================================================================================
def dump(filename, atomtype ,x,y,z):
    newfile = open(filename, 'w')
    line = 'ITEM: TIMESTEP'+'\n'
    newfile.write(line)
    line = '0'+'\n'
    newfile.write(line)
    line = 'ITEM: NUMBER OF ATOMS'+'\n'
    newfile.write(line)
    line = str(len(x))+'\n'
    newfile.write(line)            
    line = 'ITEM: BOX BOUNDS pp pp pp'+'\n'
    newfile.write(line)
    line = str(np.min(x))+' '+str(np.max(x))+'\n'
    newfile.write(line)
    line = str(np.min(y))+' '+str(np.max(y))+'\n'
    newfile.write(line)
    line = str(np.min(z))+' '+str(np.max(z))+'\n'
    newfile.write(line)
    line = 'ITEM: ATOMS id type element xu yu zu'+'\n'
    newfile.write(line)
    for i in range(len(x)):
        if( atomtype[i]== 1):
            element = 'Mg'
        else:
            element = 'O'
        line = '%8i %4i %4s %16.8f %16.8f %16.8f\n'%(i+1, atomtype[i], element, x[i], y[i], z[i])
        newfile.write(line)
    newfile.close()

#===============================================================================================
filename = sys.argv[1]     # specify data file

#===============================================================================================
s = open(filename).read()
s = s.replace('Mg', '1')
s = s.replace('O', '2')
f = open(filename, 'w')
f.write(s)
f.close()
print("Sucessfully replaced atoms type!")
print(common,end='')

#===============================================================================================
angle    = float(input("rotation angle (units in degree) : "))
angle2rad= angle/180*np.pi
a        = np.sin(angle2rad)
b        = np.cos(angle2rad)
#print('mp.sin(45) = ', np.sin(45/180*np.pi))
matrix = np.zeros((3,3))
matrix = np.array([[1, 0 , 0], [0, b, -a], [0 , a, b]])
#print('matrix = ', matrix)

data = np.loadtxt(filename,usecols=(1,2,3,4),skiprows=2)
coords = data[:,0:3]
#for i in range(len(data)):  ### test coords = data[:,0:3]
#    print("data[0] = %10.8f" %data[i,0], 'coords[0] = %10.8f' %coords[i,0])

data_new = np.zeros((len(data), 3))
for i in range(len(data)):
    for j in range(3):
        data_new[i][j] = np.dot(matrix[j], coords[i])
print(common+"Sucessfully rotate atoms!")

dumpfile = 'dump.'+filename
dump(dumpfile, data[:,3], data_new[:,0], data_new[:,1], data_new[:,2])

print(common+"Sucessfully write dumpfile : %s" %dumpfile)
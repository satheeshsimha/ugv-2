import numpy as np
import mpmath as mp
import math as ma
import matplotlib.pyplot as plt
from numpy import linalg as LA
import subprocess
import shlex
def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
A = np.loadtxt('A.dat') 
m = np.loadtxt('m1.dat')
##Generating the line 
x_mA = line_dir_pt(m,A,-8,3)
#Plotting all lines
plt.plot(x_mA[0,:],x_mA[1,:],label='Line equation')




#Labeling the coordinates
tri_coords = np.vstack((A,)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show() 

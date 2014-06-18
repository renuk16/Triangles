import matplotlib
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import scipy.interpolate
from pylab import *

import matplotlib.cbook as cbook
import matplotlib.tri as mtri

# Data to plot triangular grid
data=np.loadtxt("grid.dat")

# Create  & plot triangulation.
triang = mtri.Triangulation(data[:,0], data[:,1])
plt.triplot(triang, color='0.5')

#Load the exclusion limits data in the form: BRa BRb BRc limit. 
#This is in principle the result of running your dedicated code implementing the analysis.
'''
data3=np.loadtxt("simplestgtri.dat")
a = data3[:,0]
b = data3[:,1]
c = data3[:,2]

x=(2*b + c)/2
y=sqrt(3)*c/2

mg = data3[:,3]
'''
#Drawing the medians if necessary
'''
plt.plot([0.5,0.5], [0, 0.866], 'ko-')
plt.plot([0.25,1], [0.433, 0], 'ko-')
plt.plot([0,0.75], [0, 0.433], 'ko-')
'''
#Two sample points
'''
plt.plot(0.5, 0.288,'b*', markersize=15)
plt.plot(0.3, 0.173, 'ro', markersize=10)
plt.plot(0.01,0, 'wo', markersize=5)
'''

#Building the griddata by interpolating between the grid points 
'''
# just an arbitrary number for grid point
ngrid = 300

# you could use x.min()/x.max() for creating xi and y.min()/y.max() for yi
xi = np.linspace(x.min(),x.max(),ngrid)
yi = np.linspace(y.min(),y.max(),ngrid)

# create the grid data for the contour plot
zi = mlab.griddata(x,y,mg,xi,yi, interp='linear')

#CS3 = plt.contourf(xi, yi, zi, levels=[800,900,950,1000,1050,1100,1150,1200],cmap=plt.cm.winter, extend='both')
#plt.colorbar(CS3, anchor=(0.8,0.1))
'''
#Vertex Labels
#plt.text(-0.1,-0.02, r'$g \tilde{\chi}^0_1$ ', fontsize=20)
#plt.text(1.02,-0.02,r'$ b \bar{b} \tilde{\chi}^0_1$', fontsize=20)
#plt.text(0.48,0.88,r'$t \bar{t} \tilde{\chi}^0_1$', fontsize=20)
plt.text(-0.07,-0.02, r'$\mathcal{B}_A$ ', fontsize=20)
plt.text(1.02,-0.02,r'$\mathcal{B}_B$', fontsize=20)
plt.text(0.48,0.88,r'$\mathcal{B}_C$', fontsize=20)

#grid labels
plt.text(0.11,0.18, '0.2')
plt.text(0.21,0.35, '0.4')
plt.text(0.31, 0.52, '0.6')
plt.text(0.41,0.69, '0.8')
plt.text(0.85,0.173, '0.8', rotation=60)
plt.text(0.75,0.34, '0.6', rotation=60)
plt.text(0.65, 0.51, '0.4', rotation=60)
plt.text(0.55,0.69, '0.2', rotation=60)
plt.text(0.18,0.04, '0.8',rotation=-60)
plt.text(0.38,0.04, '0.6', rotation=-60)
plt.text(0.58, 0.04, '0.4', rotation=-60)
plt.text(0.78,0.04, '0.2', rotation=-60)
plt.ylim(-0.05,0.9)
plt.axis('off')

plt.show()

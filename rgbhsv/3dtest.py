from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
import time
import cv2

V = 1

X = np.arange(0, 10, 1)
Y = np.arange(0, 10, 1)
Z = np.arange(0, 10, 1)
X, Y, Z = np.meshgrid(X, Y, Z)

R = np.ones((10, 10)).astype(int)
R = R * 10


for r in range(10):
        for c in range(10):
            for h in range(10):
                xv = X.item(r, c, h)
                yv = Y.item(r, c, h)
                zv = Z.item(r, c, h)
                
                R.itemset((r, c), max(xv, yv, zv))
           
Z = R

#print X
#print Y
#print Z

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()
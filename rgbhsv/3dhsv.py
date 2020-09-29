import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import cv2

hsv_h = 120
hsv_s = 255
hsv_v = 150
hsv_i = ([[[hsv_h, hsv_s, hsv_v]]])

X = np.arange(0, 255, 1)
Y = np.arange(0, 255, 1)

i = 1
while i < 256:
    temp = np.uint8([[[X, Y, i]]])
    A = cv2.cvtColor(temp, cv2.COLOR_BGR2HSV)
    if A[[[2]]] == hsv_v:
        Z = i
    i += 1


fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()
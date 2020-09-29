import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
import time
import cv2

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

V = 155

fig = plt.figure()
ax = fig.add_subplot(211, projection='3d')

for r in range(255):
        for c in range(255):
            for h in range(255):
                if max(r, c, h) == V:
                    rgb = (r, c, h)
                    col = rgb_to_hex(rgb)
                    ax.plot([r],[c],[h],'*', color = col)
                    
ax.grid(True)
ax.set_title('BGR')
plt.xlim((0,255))
plt.ylim((0,255))

plt.show()


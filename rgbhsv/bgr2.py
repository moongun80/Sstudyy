import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
import time
import cv2

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

V = 200

fig = plt.figure()
ax = fig.add_subplot(211, projection='3d')

for h in range(180):
        for s in range(255):
                v = V
                hsv = np.uint8([[[h, s, v]]])
                rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
                                              
                r, g, b = rgb[0, 0, 0], rgb[0, 0, 1], rgb[0, 0, 2]
                temp = (r, g, b)
                col = rgb_to_hex(temp)
                ax.plot([r], [g], [b], '*', color = col)
                    
ax.grid(True)
ax.set_title('BGR')
plt.xlim((0,255))
plt.ylim((0,255))

plt.show()



import cv2
import numpy as np
from matplotlib import pyplot as plt

def display_histogram():
    img = cv2.imread('raspberrypi.jpg')

    # calculate histogram in OpenCV
    # and plotting histogram with its color
    color = ('b', 'g', 'r')
    for i,col in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0,256])
        plt.plot(hist, color = col)
        plt.xlim([0,256])
    plt.show()

if __name__ == "__main__":
    display_histogram()
    

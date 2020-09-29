import numpy as np
import cv2

def rgb2hsv():
    b = np.uint8([[[100, 205, 55]]])
    g = np.uint8([[[60, 255, 255]]])
    r = np.uint8([[[0, 255, 255]]])

    hsv_b = cv2.cvtColor(b, cv2.COLOR_HSV2BGR)
    hsv_g = cv2.cvtColor(g, cv2.COLOR_HSV2BGR)
    hsv_r = cv2.cvtColor(r, cv2.COLOR_HSV2BGR)

    print ('HSV for blue: ' , hsv_b)
    print ('HSV for green: ' , hsv_g)
    print ('HSV for red: ' , hsv_r)
    
def main():
  rgb2hsv()
  
if __name__ == "__main__" :
    main()

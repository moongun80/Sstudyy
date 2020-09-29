# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from copy import deepcopy
import numpy as np
import time
import cv2

def invert_image1(image):
    dest = deepcopy(image)

    e1 = cv2.getTickCount()
    rows, cols, ch = image.shape
    for r in range(rows):
        for c in range(cols):
            rv = dest.item(r, c, 2)
            gv = dest.item(r, c, 1)
            bv = dest.item(r, c, 0)

            dest.itemset((r, c, 2), 255-rv)
            dest.itemset((r, c, 1), 255-gv)
            dest.itemset((r, c, 0), 255-bv)

    e2 = cv2.getTickCount()
    etime = (e2 - e1) / cv2.getTickFrequency()
    print ('processing time : ', etime)

    return dest

def invert_image2(image):
    dest = deepcopy(image)
    e1 = cv2.getTickCount()

    dest = 255-dest

    e2 = cv2.getTickCount()
    etime = (e1 - e2)/ cv2.getTickFrequency()
    print (' processing time : ', etime)

    return dest

def rgb2hsv():
    b = np.uint8([[[255, 0, 0]]])
    g = np.uint8([[[0, 255, 0]]])
    r = np.uint8([[[0, 0, 255]]])

    hsv_b = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)
    hsv_g = cv2.cvtColor(g, cv2.COLOR_BGR2HSV)
    hsv_r = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)

    print ('HSV for blue: ' , hsv_b)
    print ('HSV for green: ' , hsv_g)
    print ('HSV for red: ' , hsv_r)

def main():
  rgb2hsv()
  # initialize the camera and grab a reference to the raw camera capture
  camera = PiCamera()
  camera.resolution = (640, 480)
  camera.framerate = 32
  rawCapture = PiRGBArray(camera, size=(640, 480))
  # allow the camera to warmup
  time.sleep(0.1)
  # capture frames from the camera
  for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw Numpy array representing the image,
        # then initialize the timestamp and occupied/unoccupied text
        image = frame.array
        result = invert_image2(image)
       # result = image
        
        # show the frame
        cv2.imshow("frame", result)
        key = cv2.waitKey(1) & 0xFF             # in 64bit machine

        # clear the stream in prparation for the next frame
        rawCapture.truncate(0)

        # if the  'q' key was pressed, break from the loop
        if key == ord("q"):
            break
        elif key == ord("s"):
            cv2.imwrite("copy.jpg", result)

if __name__ == "__main__" :
    main()


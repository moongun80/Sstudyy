# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from copy import deepcopy
import time
import cv2
import numpy as np

def extract_region(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define range of blule color in HSV
    lower_blue = np.array([20, 40, 40])
    upper_blue = np.array([150, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    dest = cv2.bitwise_and(image, image, mask = mask)

    return dest

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
    print('processing time : ', etime)

    return dest

def invert_image2(image):
    dest = deepcopy(image)
    e1 = cv2.getTickCount()

    dest = 255-dest

    e2 = cv2.getTickCount()
    etime = (e1 - e2)/ cv2.getTickFrequency()
    print (' processing time : ', etime)

    return dest

def main():
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
        result2 = extract_region(image)
       # result = image
        
        # show the frame
        cv2.imshow("frame", result)
        cv2.imshow("frame2", result2)
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


import time
from picamera import PiCamera
from picamera.array import PiRGBArray
from copy import deepcopy
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
    print ('processing time: ', etime)

    return dest

def invert_image2(image):
    dest = deepcopy(image)
    e1 = cv2.getTickCount()

    dest = 255-dest

    e2 = cv2.getTickCount()
    etime = (e2-e1) / cv2.getTickFrequency()
    print ('processing time: ', etime)

    return dest 

def handle_roi(image):
    dest = deepcopy(image)

    rows, cols, ch = dest.shape

    half_rows = rows / 2
    half_cols = cols / 2
    
    dest[0: int(half_rows), 0: int(half_cols)] = image[0: int(half_rows), 0: int(half_cols)] * (1, 1, 0)

    return dest

def handle_channel1(image, ch='r'):
    e1 = cv2.getTickCount()
    b, g, r = cv2.split(image)

    if(ch == 'r'):
        result = r
    elif(ch == 'g'):
        result = g
    elif(ch == 'b'):
        result = b
    else:
        result = image

    e2 = cv2.getTickCount()
    etime = (e2 - e2) / cv2.getTickFrequency()
    print ('processing time: ', etime)

    return result

def handle_channel2(image, ch='r'):
    e1 = cv2.getTickCount()
    if(ch == 'r'):
        result = image[:, :, 2]
    elif(ch == 'g'):
        result = image[:, :, 1]
    elif(ch == 'b'):
        result = image[:, :, 0]
    else:
        result = image
    e2 = cv2.getTickCount()
    etime = (e1 - e2) / cv2.getTickFrequency()
    print ('processing time: ', etime)

    return result

def main():
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640,480))

    # allow the camera to warm up
    time.sleep(0.1)
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array represnting the image,
        # then initialize the timestamp and occupied/unoccupied text
        image = frame.array
       # result = invert_image2(image)
        #result = handle_roi(image)
        result1 = handle_channel2(image, ch='b')
        result2 = handle_channel2(image, ch='g')
        result3 = handle_roi(image) 
        
        # show the frame
        cv2.imshow("frame1", result1)
        cv2.imshow("frame2", result2)
        cv2.imshow("frame3", result3)
        cv2.imshow("original",image)
        key = cv2.waitKey(1) & 0xFF       # in 64bit machine

        # clear the stram in preparation for the next frame
        rawCapture.truncate(0)

        # if the 'q' key was pressed, break from the loop
        if key == ord("q"):
            break
        elif key == ord("s"):
            cv2.imwrite("raspberry.jpg", result3)
if __name__ == "__main__" :
    main()


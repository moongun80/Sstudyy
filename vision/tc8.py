import time
from picamera import PiCamera
from picamera.array import PiRGBArray
from matplotlib import pyplot as plt
import cv2
import numpy as np

def main():
    # initialize the camera and grab a reference to 
    # the raw camera capture
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))

    # allow the camera to warmup
    time.sleep(0.1)

    fig1 = fig2 = fig3 = fig4 = None
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        org, blur, grad, edge = proc_image(image)

        if fig1 is None:
            plt.subplot(221)
            fig1 = plt.imshow(org)
            plt.title('Org'), plt.xticks([]), plt.yticks([])

            plt.subplot(222)
            fig2 = plt.imshow(blur)
            plt.title('Blur'), plt.xticks([]), plt.yticks([])

            plt.subplot(223)
            fig3 = plt.imshow(grad, 'gray')
            plt.title('Gradient'), plt.xticks([]), plt.yticks([])

            plt.subplot(224)
            fig4 = plt.imshow(edge, 'gray')
            plt.title('Edge'), plt.xticks([]), plt.yticks([])

        else:
            fig1.set_data(org)
            fig2.set_data(blur)
            fig3.set_data(grad)
            fig4.set_data(edge)

        plt.draw()
        flag = plt.waitforbuttonpress(0.05)

        # clear the stream in prepatarion for the next frame
        rawCapture.truncate(0)

        if flag == True:
            break

def proc_image(image):
    dst1 = cv2.GaussianBlur(image, (5,5), 0)
    dst1 = cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst2 = cv2.Laplacian(gray, cv2.CV_64F)
    dst3 = cv2.Canny(gray, 70, 200)
    org = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return org, dst1, dst2, dst3

if __name__== "__main__":
    main()


         
          


import logging
import math
import time

from adafruit_servokit import ServoKit
from picamera import PiCamera


# https://github.com/pimoroni/pantilt-hat/blob/master/examples/smooth.py


def camera_test(rotation):
    camera = PiCamera()
    camera.rotation = rotation
    logging.info('Starting Raspberry Pi Camera')
    camera.start_preview()

    try:
        while True:
            continue
    except KeyboardInterrupt:
        logging.info('Stopping Raspberry Pi Camera')
        camera.stop_preview()


def pantilt_test():
    logging.info('Starting Pan-Tilt HAT test!')
    logging.info('Pan-Tilt HAT should follow a smooth sine wave')
    
    kit = ServoKit(channels=16)
    kit.servo[0].set_pulse_width_range(500, 2700)
    kit.servo[1].set_pulse_width_range(700, 1700)


    while True:
        # Get the time in seconds
        t = time.time()

        # G enerate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
        a = math.sin(t * 2) * 90 + 90
        b = math.cos(t * 2) * 90 + 90
        # Cast a to int for v0.0.2
        a = int(a)
        b = int(b)
        kit.servo[0].angle = a
        kit.servo[1].angle = b

        # Sleep for a bit so we're not hammering the HAT with updates
        time.sleep(0.005)


if __name__ == '__main__':
    pantilt_test()
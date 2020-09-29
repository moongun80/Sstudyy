import time
from adafruit_servokit import ServoKit
     
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(500, 2700)

kit.servo[0].angle = 0

time.sleep(1)
kit.servo[0].angle = 30

time.sleep(1)
kit.servo[0].angle = 60

time.sleep(1)
kit.servo[0].angle = 90

time.sleep(1)
kit.servo[0].angle = 120

time.sleep(1)
kit.servo[0].angle = 150

time.sleep(1)
kit.servo[0].angle = 180

time.sleep(1)
exit()
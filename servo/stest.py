import time
from adafruit_servokit import ServoKit
     
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

kit.servo[0].set_pulse_width_range(500, 2700)
kit.servo[1].set_pulse_width_range(700, 1700)

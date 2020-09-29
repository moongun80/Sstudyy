import time
from adafruit_servokit import ServoKit
     
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

kit.servo[0].set_pulse_width_range(500, 2700)
kit.servo[1].set_pulse_width_range(700, 1700)

kit.servo[0].angle = 0
kit.servo[1].angle = 0
time.sleep(1)
kit.servo[0].angle = 30
kit.servo[1].angle = 30
time.sleep(1)
kit.servo[0].angle = 60
kit.servo[1].angle = 60
time.sleep(1)
kit.servo[0].angle = 90
kit.servo[1].angle = 90
time.sleep(1)
kit.servo[0].angle = 120
kit.servo[1].angle = 120
time.sleep(1)
kit.servo[0].angle = 150
kit.servo[1].angle = 150
time.sleep(1)
kit.servo[0].angle = 180
kit.servo[1].angle = 180
time.sleep(1)
kit.servo[0].angle = 0
kit.servo[1].angle = 0
time.sleep(1)
kit.servo[0].angle = 180
kit.servo[1].angle = 0
time.sleep(1)
kit.servo[0].angle = 0
kit.servo[1].angle = 180
time.sleep(1)
kit.servo[0].angle = 180
kit.servo[1].angle = 180
time.sleep(1)

kit.continuous_servo[2].throttle = 1
time.sleep(1)
exit()
#kit.continuous_servo[0].throttle = 1
#kit.continuous_servo[1].throttle = -1
#time.sleep(1)
#kit.servo[0].angle = 0
#kit.continuous_servo[1].throttle = 0
from reset_motor import resetXY
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(address = 0x61)

for i in range(4000):
        # kit.stepper1.onestep(direction = stepper.FORWARD, style = stepper.SINGLE)
        kit.stepper2.onestep(direction = stepper.BACKWARD, style = stepper.SINGLE)

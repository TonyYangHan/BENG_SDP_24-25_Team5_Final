from reset_motor import resetXY
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(address = 0x61)

def go_to_first():
    resetXY()

    for i in range(1200):
        kit.stepper1.onestep(direction = stepper.FORWARD, style = stepper.SINGLE)
        kit.stepper2.onestep(direction = stepper.BACKWARD, style = stepper.SINGLE)
    
    # for i in range(400):
    #     kit.stepper2.onestep(direction = stepper.BACKWARD, style = stepper.SINGLE)

if __name__ == "__main__":
    go_to_first()
    
    
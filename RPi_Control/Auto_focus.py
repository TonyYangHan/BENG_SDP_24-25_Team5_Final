from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import cv2, time, subprocess as sp

# 2500-3500 steps seem to be the best focus range (beads with water, cell phone light)
# 3150 (3100-3300) from the bottom, or 1850 from top gives the best focus
# shutter = 40000 (15000 with max bright)gain = 30-35 for totally dark condition with 4 corner LEDs parallel (100 Ohms)
# shutter = 15000, gain = 20 with maximum brightness of ambient light and no top light
# shutter = 13000, gain = 10 finds a balance between top light (constrast) and ambient illumination.
# shutter = 18000, gain = 20 for the black top (very good contrast)

# Initialize Motor Kit and Camera
kit = MotorKit(address = 0x60)

# Function to calculate image sharpness
def calculate_sharpness(ip):
    gray = cv2.cvtColor(cv2.imread(ip), cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian

# Autofocus routine
def autofocus(stride = 50, move_range = 1000):
    max_sharpness = 0
    best_position = 0

    for i in range(0, move_range, stride):  # Limit the number of steps

        path_name = f"z_images/z-pos_{i}.jpg"
        iso = 100
        cmd = ["libcamera-still", "-o", path_name, "--nopreview", "--shutter", "18000", "--gain", "20",
               "--timeout", "2000"] # optimal settings for beads with z height at 3000 from origin
        sp.run(cmd, check = True)
        sharpness = calculate_sharpness(path_name)
        
        print(f"Position: {i}, Sharpness: {sharpness}")

        # Check if this position is the best
        if sharpness > max_sharpness:
            max_sharpness = sharpness
            best_position = i

        for i in range(stride):
            kit.stepper1.onestep(direction = stepper.BACKWARD)
            kit.stepper2.onestep(direction = stepper.BACKWARD)
    
    for i in range(move_range-best_position):
        kit.stepper1.onestep(direction = stepper.FORWARD)
        kit.stepper2.onestep(direction = stepper.FORWARD)

    print(f"Best focus position: {best_position}")

# Run autofocus
autofocus()

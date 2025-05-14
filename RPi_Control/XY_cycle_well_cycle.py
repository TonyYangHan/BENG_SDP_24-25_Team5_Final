from reset_motor import resetXY
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time, subprocess

# coords are (x,y) system, viewing from the direction where the notes on the tape are inverted
# x difference between consecutive plates = 4000, also y_diff = 4000
# stepper motor 1 backward and stepper motor 2 forward goes to origin (negative direction)

# Imaging area: 475 steps along y, 410 steps along x(+-30 steps)
# coord_center = [(0,0), (950,0),(4950,0),(8950,0),(8950,4000),(4950,4000),(950,4000)]
coord = [(0,0), (100,400),(4100,400),(8100,400),(8100,4400),(4100,4400),(100,4400)]
fov = (440,505) # Slightly larger than actual FOV to ensure images does not overlap

kit = MotorKit(address = 0x61)

def image_capture(file_name):

    command = ["libcamera-still", "-o", file_name, "--nopreview", 
                   "--shutter", "40000", "--gain", "35"]
    subprocess.run(command, check=True)

    return

def from_to(start, end, step_wait):

    if start[0] < 0 or start[1] < 0 or end[0] < 0 or end[1] < 0:
        print("Negative coordinate received, aborting the move")
        return
    
    x_diff, y_diff = end[0] - start[0], end[1] - start[1]

    # Move along one direction at a time
    while x_diff > 0:
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        x_diff -= 1
        time.sleep(step_wait)
    while x_diff < 0:
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        x_diff += 1
        time.sleep(step_wait)

    while y_diff > 0:
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        y_diff -= 1
        time.sleep(step_wait)
    while y_diff < 0:
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        y_diff += 1
        time.sleep(step_wait)
    return

def image_well(global_coord, well_num, wait):
    count = 1
    prev_dest = global_coord

    for _ in range(5):
        dest = (prev_dest[0] + fov[0], prev_dest[1])
        from_to(prev_dest, dest, wait)

        image_capture(f"temp_img_cache/well_{well_num}_img_{count}.jpg")
        count += 1
        prev_dest = dest
    
    new_dest = (dest[0], dest[1] + fov[1])
    from_to(dest, new_dest, wait)
    image_capture(f"temp_img_cache/well_{well_num}_img_{count}.jpg")
    count += 1
    prev_dest = new_dest

    for _ in range(5):
        new_dest = (new_dest[0] - fov[0], new_dest[1])
        from_to(prev_dest, new_dest, wait)
        image_capture(f"temp_img_cache/well_{well_num}_img_{count}.jpg")
        count += 1
        prev_dest = new_dest
    
    new_dest2 = (new_dest[0], new_dest[1] + fov[1])
    from_to(new_dest, new_dest2, wait)
    image_capture(f"temp_img_cache/well_{well_num}_img_{count}.jpg")
    count += 1
    prev_dest = new_dest2

    for _ in range(5):
        new_dest2 = (new_dest2[0] + fov[0], new_dest2[1])
        from_to(prev_dest, new_dest2, wait)
        image_capture(f"temp_img_cache/well_{well_num}_img_{count}.jpg")
        count += 1
        prev_dest = new_dest2
    
    from_to(new_dest2, global_coord, wait)
    image_capture(f"temp_img_cache/well_{well_num}_img_{count}.jpg")

    return

def XY_cycle(step_wait = 0.001):
    resetXY()

    for i in range(len(coord)-1):
        from_to(coord[i], coord[i+1], step_wait)
        image_well(coord[i+1], i+1, step_wait)
    
    return

if __name__ == "__main__":
    XY_cycle()
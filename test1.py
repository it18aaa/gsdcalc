# Nadir and Oblique Footprint and GSD Calculator
# Ian Thomson 2023
#

import math

height = 348

focal_length = 80
fov_long = 30.4
fov_short = 23
sensor_long = 12_768   #  pixels in sensor long side
sensor_short = 9_564   # pixels in sensor short side

megapix = sensor_long * sensor_short / 1_000_000  # sensor size in megapixels

gsd_basic = height / (focal_length * 1000)

nad_width = 2 * (height * math.tan(math.radians(fov_long/2)))
nad_height = 2 * (height * math.tan(math.radians(fov_short/2)))


obl_angle = 30  # angle camera is point at, off nadir
obl_near = obl_angle - (fov_long/2)  # near angle from nadir
obl_far = obl_angle + (fov_long/2)   # far angle from nadir

dist_near = height / math.cos(math.radians(obl_near))  
dist_far = height / math.cos(math.radians(obl_far))

proj_obl_near = dist_near * math.sin(math.radians(obl_near)) 
proj_obl_far = dist_far * math.sin(math.radians(obl_far))
proj_obl_width_near = 2 * (dist_near * math.tan(math.radians(fov_short/2)) ) 
proj_obl_width_far = 2 * (dist_far * math.tan(math.radians(fov_short/2)) ) 

print(f"Height {height}m")
print(f"Long FOV angle {fov_long}")
print(f"Short FOV angle {fov_short}")

print(f"Nadir footprint is {nad_width:.2f}m by {nad_height:.2f}")

print(f"Oblique Near Angle {obl_near:.2f}")
print(f"Oblique Far Angle {obl_far:.2f}")

print(f"nearest distance is {dist_near:.2f}m")
print(f"furthest distance is {dist_far:.2f}m")

print(f"Oblique is {proj_obl_near:.2f}m to {proj_obl_far:.2f}m from perp")
print(f"with a near width of {proj_obl_width_near:.2f}m and a far width of {proj_obl_width_far:.2f}m")


print(f"Sensor is {megapix:.2f} megapixels")

print(f"GSD Basic is {gsd_basic}")
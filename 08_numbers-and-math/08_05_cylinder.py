# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

# Volume = V=πr2h
# Surface Area A=2πrh+2πr2


import math

r = 3.14
h = 5

v = math.pi * r ** 2 * h
a = (2 * math.pi * r * h) + (2 * (math.pi * r ** 2))

print("Volume of Cylinder", v)
print("Surface Area of Cylinder", a)
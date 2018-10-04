import math

# Read radius from user
print("Please enter radius")
radius = float(input())
radiussquared =radius**2
# The **2 function lets us square
# Alternative pow(radius, 2)

# Calculate the area
area = math.pi * radiussquared
print("The area is", round(area, 2))

# Calculate the circumference
circ = int(2) * math.pi * radius
print("The circumference is", round(circ, 2))

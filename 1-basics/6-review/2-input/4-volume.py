import math

print("Let's calcualate the volume (cyclinder/cone)")
print("Pick a cylinder or cone.")
shape = str(input())
print("Enter the radius.")
radius = float(input())
print("Enter the height.")
height = float(input())

# Using if, else and elif statements
if shape == "cylinder" :
  volume = (math.pi * (radius**2) * height)

  print(volume, "is the volume of your cylinder. (", round(volume, 2),"rounded to 2 dp. )")

elif shape == "cone":
  volume = (math.pi * (radius**2) * height)/ 3
  print(volume, "is the volume of your cone. (", round(volume, 2),"rounded to 2 dp. )")

else:
  print("I don't know what you mean.")

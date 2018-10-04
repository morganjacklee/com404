# Read direction from user
print("Please enter one of the following directions")
print("W is to go up.")
print("S is to go down.")
print("A is to go left.")
print("D is to go right.")
direction = str(input())

# Using if, else and elif statements
if direction == "w":
  print("You are moving up.")
elif direction == "d":
  print("You are moving right.")
elif direction == "a":
  print("You are moving left.")
elif direction == "s":
  print("You are moving down.")
else :
  print ("I don't know where you are going!")

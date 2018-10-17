# Defining a function that is user generated
def play():
  print("I have lots of toys to play with.")
def movie():
  print("Watching a movie sounds like fun")

# Read activity from user
print("What activity do you want to do")
activity = str(input())

# Using if, else and elif statements
if activity == "Play":
  play()
elif activity == "Watch movie":
  movie()
else :
  print ("I am not sure if I will like it but I will give it a try.")

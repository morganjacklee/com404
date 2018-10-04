# The modulo operator returs the remainder after division
# e.g. 4 % 2 returns 0
# e.g. 5 % 3 returns 2
# e.g. 10 % 4 returns 2

# If a number is even it divides by 2 and has no remainder


print("Please enter a number, I will work out whether it is even or odd.")
number = int(input())

calc = number % 2

# Using if, else and elif statements
if calc == int(0) :
  print("This is an even number.")
else :
  print ("This is an odd number.")

# Comparing two numbers
print("Tell me two numbers, I will tell you the largest.")

print("Please enter the first number.")
first_number = float(input())

print("Please enter the second number")
second_number = float(input())

# Using if, else and elif statements
if (first_number > second_number):
  print("The first number is the largest.")
elif (first_number < second_number):
  print ("The second number is largest.")
else:
  print ("The numbers are equal.")

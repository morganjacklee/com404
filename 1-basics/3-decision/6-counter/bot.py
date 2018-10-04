print("Tell me three numbers, I will tell you how many are even and odd.")

print("Please enter a number.")
first_number = float(input())

print("Please enter a number.")
second_number = float(input())

print("Please enter a number.")
third_number = float(input())

calc_one = first_number % 2
calc_two = second_number % 2
calc_three = third_number % 2

count = 0
secondcount = 0 

# Using if, else and elif statements
if calc_one == int(0) :
  count = count + 1
else :
  secondcount = secondcount + 1
  
if calc_two == int(0) :
  count = count + 1
else :
  secondcount = secondcount + 1

if calc_three == int(0) :
  count = count + 1
else :
  secondcount = secondcount + 1


print("There are", count, "even number(s) and", secondcount, "odd number(s).")

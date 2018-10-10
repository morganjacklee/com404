# Bring in integer chosen by user
print("Please enter a number")
number = int(input())

# Easiest to count using 1 as stepping stone
factorial = 1

# Saving in the variable after each, calculating the factorial, saving in variable.
# Always counts up until it reaches the number defined.
for times in range(1, number + 1):
    factorial = factorial * times
 
print("The factorial of your number is ", factorial)

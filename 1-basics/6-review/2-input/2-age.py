import math

# Constants are for readability and maintainability
DAYS_IN_YEAR = float(365.25)

# Ask age of user
print("What is your age in years?")
years = int(input())

# Calculate in days
days = DAYS_IN_YEAR * years

# Print the days
print("That is", round(days, 2),  "days.")

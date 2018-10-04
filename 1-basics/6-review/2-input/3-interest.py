import math

DAYS_IN_YEAR = float(365.25)

# Read current amount from user
print("Current savings: (£)")
current_savings = float(input())

# Read interest rate from user
print("Interest rate; (%)")
interest_rate = float(input())

# Calculate interest new amount
interest_amount = (interest_rate / 100) * current_savings
new_amount = current_savings + interest_amount

# Print the total interest amount
print("That is £", round(new_amount, 2),  "with interest included")

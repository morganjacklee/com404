# Read user data
print("Enter your name:")
name = input()
print("Enter your age:")
age = int(input())
print("Enter your height:")
height = float(input())
print("Enter your weight (kg):")
weight = float(input())

total = weight / (height * height)
print(name+", your BMI is...",total)

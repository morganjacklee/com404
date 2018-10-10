# Take string input and use the len function to record in variable the length.
print("What shall I repeat?")
message = str(input())
number = len(message)

print("I'm going to repeat", message, "for", number, "times.")

for count in range(0,number, 1):
  print(message)

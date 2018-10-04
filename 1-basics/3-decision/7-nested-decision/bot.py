print("Where shall I look?")
print("Choices are:")
print("""- Bedroom
- Bathroom
- Labratory
- Somewhere else""")
location = str(input())

# Using if, else and elif statements
if location == "Bedroom" :
  print("Where in the bedroom?")
  print("""- Under the bed
- Somewhere else""")
  location_bedroom = str(input())
  if location_bedroom == "Under the bed" :
    print("Found some socks but no battery.")
  elif location_bedroom == "Somewhere else" :
    print("Found some mess but no battery.")
elif location == "Bathroom":
  print("Not in the bathroom!")
elif location == "Labratory":
  print("Not in the labratory!")
elif location == "Somewhere else":
  print("Found some mess but no battery")
else:
  print("I don't know what you mean!")

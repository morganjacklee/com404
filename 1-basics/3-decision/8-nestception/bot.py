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
  print("Where in the bathroom?")
  print("""- In the Bathtub
- Somewhere else""")
  location_bathroom = str(input())
  if location_bathroom == "In the bathtub" :
    print("Found a rubber duck but no battery.")
  elif location_bathroom == "Somewhere else" :
    print("It's wet and there is no battery.")
elif location == "Labratory":
  print("Where in the labratory?")
  print("""- On the table
- Somewhere else""")
  location_labratory = str(input())
  if location_labratory == "On the table" :
    print("Found the battery!")
  elif location_labratory == "Somewhere else" :
    print("Found some tools but no battery.")
elif location == "Somewhere else":
  print("I don't know where that is but I will keep looking!")
else:
  print("I'm not sure what you mean!")

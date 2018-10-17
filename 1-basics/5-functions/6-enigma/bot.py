def run():
  print("Please enter a character to display...")
  char = str(input())

  print("Please enter total number of characters...")
  total = int(input())

  print("Please enter a whole number")
  number = int(input())
  
  for count in range(1,total, 1):
    if count % number == 0 :
      print(char, end="")
    else:         
      print("-", end="")

      


# Run the program
run()

AMOUNT = 10


print("How many ascii robots shall I draw?")
robots = int(input())


print("Here I go")

if robots < int(10) :
  for count in range(0,robots, 1):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")

    robots = -1
else:
  for count in range(0,AMOUNT, 1):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")

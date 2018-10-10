AMOUNT = 10

empty = 0

print("How many ascii robots shall I draw?")
robots = int(input())


if robots < AMOUNT :
  while (robots > empty):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")

    robots = robots - 1
else:
  total = 0
  while (AMOUNT > total):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")

    total = total + 1


print("How many rows should I have?")
rows = int(input())

print("How many columms should I have?")
columns = int(input())

for count in range(0, rows, 1):
    for number in range(0, columns, 1):
        print(":)", end="")
    print()

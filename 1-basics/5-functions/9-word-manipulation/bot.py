def display_box(text):
  print("*" * (len(text) + 10))
  print("*", text, "*")
  print("*" * (len(text) + 10))

def display_lower(text):
  print(text.lower())

def display_upper(text):
  print(text.upper())

def display_mirrored(text):
  for position in range(len(text)-1, -1, -1):
	  print(text[position], end="")


def display_repeat(text):
  print("How many times?")
  number = int(input())

  for count in range(0,number, 1):
    if count % 2 == 0 :
      print(text.upper())
    else:         
      print(text.lower())


def greet_user():
    print("Please enter a word to manipulate:")
    text = str(input())

    pick = True
    while pick == True:
      print("Please pick from the following: (1-5)")
      print("""1) Display in a Box – display the word in an ascii art box
2) Display Lower-case – display the word in lower-case e.g. hello
3) Display Upper-case – display the word in upper-case e.g. HELLO
4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
5) Repeat – how many times to display the word and then display the word that many times alternating between upper-case and lower-case.""")
      choice = str(input())
      if choice == "1":
        pick = False
        display_box(text)
      elif choice == "2":
        pick = False
        display_lower(text)
      elif choice == "3":
        pick = False
        display_upper(text)
      elif choice == "4":
        pick = False
        display_mirrored(text)
      elif choice == "5":
        pick = False
        display_repeat(text)
  

  
  
greet_user()

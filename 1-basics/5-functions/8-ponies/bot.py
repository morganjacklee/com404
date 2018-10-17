def sum_ages_of_friends(firstage, secondage, thirdage):
  print(firstage + secondage + thirdage)
def calc_avg_age_of_friends(firstage, secondage, thirdage):
  print(firstage + secondage + thirdage / 3)


  
def run():
  pick = True
  while pick == True:
    print("Would you like to work out the average age or sum?")
    print("Please pick: (avg/sum)")
    name = str(input())
    if name == "sum":
      pick = False
      sum_ages_of_friends(2 , 3, 7)
    elif name == "avg":
      pick = False
      calc_avg_age_of_friends(2 , 3, 7)

  
run()

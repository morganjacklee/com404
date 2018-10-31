class Bot:
  
  def __init__(self, name, age=0, energy=100, shield_level=100):
    self.__name = name
    self.__age = age
    self.__energy = energy
    self.__shield_level = shield_level

# First set
  def get_age(self):
    return self.__age
  def get_energy(self):
    return self.__energy
  def get_name(self):
    return self.__name
  def get_shield(self):
    return self.__shield_level

# Second set
  def decrement_energy(self, amount):
    self.__energy = (self.__energy - amount)

  def decrement_shield(self, amount):
    self.__shield_level = (self.__shield_level - amount)

# Third set
  def display_age(self):
    print("{} is the age of the bot".format(self.__age))

  def display_energy(self):
    print("Currently {} has the energy of {}.".format(self.__name,self.__energy))

  def display_name(self):
    print("{} is the name of the bot".format(self.__name))

  def display_shield(self):
    print("The shield levels of {} are currently {}.".format(self.__name,self.__shield_level))

  def display_summary(self):
    print("{} is currently {} years old, and has the level of {} energy. The shields are currently set as {}.".format(self.__name,self.__age,self.__energy,self.__shield_level))

  def __str__(self):
    return("{} is currently {} years old, and has the level of {} energy. The shields are currently set as {}.".format(self.__name,self.__age,self.__energy,self.__shield_level))

# Fourth set
  def increment_age(self, amount):
    self.__age = (self.__age + amount)

  def increment_energy(self, amount):
    self.__energy = (self.__energy + amount)

  def increment_shield(self, amount):
    self.__shield_level = (self.__shield_level + amount)

# Fifth set
  def set_name(self, name):
    self.__name = name

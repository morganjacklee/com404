class Bot:
  
  def __init__(self, name, age=0, energy=100, shield_level=100):
    self.name = name
    self.age = age
    self.energy = energy
    self.shield_level = shield_level

# First set
  def get_age(self):
    return self.age
  def get_energy(self):
    return self.energy
  def get_name(self):
    return self.name
  def get_shield(self):
    return self.shield_level

# Second set
  def decrement_energy(self, amount):
    self.energy = (self.energy - amount)

  def decrement_shield(self, amount):
    self.shield = (self.shield - amount)

# Third set
  def display_age(self):
    print("{} is the age of the bot".format(self.age))

  def display_energy(self):
    print("Currently {} has the energy of {}.".format(self.name,self.energy))

  def display_name(self):
    print("{} is the name of the bot".format(self.name))

  def display_shield(self):
    print("The shield levels of {} are currently {}.".format(self.name,self.shield_level))

  def display_summary(self):
    print("{} is currently {} years old, and has the level of {} energy. The shields are currently set as {}.".format(self.name,self.age,self.energy,self.shield_level))

  def __str__(self):
    return("{} is currently {} years old, and has the level of {} energy. The shields are currently set as {}.".format(self.name,self.age,self.energy,self.shield_level))

# Fourth set
  def increment_age(self, amount):
    self.age = (self.age + amount)

  def increment_energy(self, amount):
    self.energy = (self.energy + amount)

  def increment_shield(self, amount):
    self.shield = (self.shield + amount)

# Fifth set
  def set_name(self, name):
    self.name = name

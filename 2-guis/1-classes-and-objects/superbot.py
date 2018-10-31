from bot import Bot

class SuperBot(Bot):

  def __init__(self, name, age=0, energy=100, shield_level=100, super_power_level=100):
    super().__init__(name, age, energy, shield_level)
    self.super_power_level = super_power_level

  def get_super_power_level(self):
    return self.super_power_level

  def set_super_power_level(self, level):
    self.super_power_level = level
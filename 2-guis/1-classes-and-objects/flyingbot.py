from superbot import SuperBot

class FlyingBot(Bot):

  def __init__(self, name, age=0, energy=100, shield_level=100, hover):
    super().__init__(name, age, energy, shield_level)
    self.hover = hover

  def get_hover_distance(self):
    return self.hover

  def set_hover_distance(self, distance):
    self.set_hover_distance = distance
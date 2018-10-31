from bot import Bot
from superbot import SuperBot

morgan = Bot("Morgan")
morgan.display_name()
morgan.display_age()
morgan.display_energy()
morgan.display_shield()
morgan.display_summary()

print("")

terry = SuperBot("Terry")
terry.display_age()
terry.increment_age(10)
terry.display_age()
terry.increment_age(10)
terry.display_age()
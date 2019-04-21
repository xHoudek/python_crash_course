from random import randint

class Die():
    """a simple representation of a die"""

    def __init__(self, sides):
        """initialized sides as an attribute"""
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)

d6 = Die(6)
d10 = Die(10)
d20 = Die(20)

for i in range(10):
    d6.roll_die()

for i in range(10):
    d10.roll_die()

for i in range(10):
    d20.roll_die()
from random import randint

class Dice:
    """Create an instance of a die with a specific amount of sides"""

    def __init__(self, sides):
        """Generate an instance of a die"""
        self.sides = sides

    def roll_die(self):
        """Method to make the die roll"""
        die_rolling = randint(1,self.sides)
        return f"The die number is {die_rolling}!"

    def roll(self,times):
        """Amount of time the die is going to roll"""
        count = 0
        attempt = 1
        while count < times:
            dice_rolling = self.roll_die()
            print(f"Attempt #{attempt} - {dice_rolling}")
            count +=1
            attempt +=1
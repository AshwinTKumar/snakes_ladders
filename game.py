import random


def roll_dice(dice_type=None):
    if dice_type == "C":
        return random.randrange(2, 13, 2)
    else:
        return random.randint(1, 6)

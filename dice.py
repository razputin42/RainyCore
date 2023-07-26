import random


def dice(roll: str) -> (int, list[int]):
    roll = roll.strip().lower()
    if "d" not in roll:  # nothing to roll, return the number
        return int(roll), None
    if roll.startswith("d"):  # only one die to roll
        n_dice = 1
        dice_type = int(roll[1:])
    else:  # multiple dice to roll
        n_dice, dice_type = roll.split("d")
        n_dice = int(n_dice)
        dice_type = int(dice_type)

    sum = 0
    rolled = []
    for i in range(n_dice):
        roll = random.randint(1, dice_type)
        sum += roll
        rolled.append(roll)

    return sum, rolled

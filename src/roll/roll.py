import re
import random


def roll(roll_input):
    roll_input = str.replace(roll_input, " ", "", -1)
    roll_input = roll_input.lower()
    if roll_input == "":
        print("No entry!")
        return
    natural = False
    advantage = False
    disadvantage = False
    if re.search("(.+?)[d]", roll_input):
        try:
            num_dice = int(re.search("(.+?)[d]", roll_input).group(1))
        except ValueError:
            num_dice = 1
    else:
        num_dice = 1
    if re.search("d(.+?)[ +]", roll_input):
        try:
            num_sides = int(re.search("d(.+?)[ +]", roll_input).group(1))
        except ValueError:
            print("Invalid Entry, number of sides not found")
            return
    elif re.search("d(.+?)", roll_input):
        try:
            num_sides = int(re.search("d(.+?)", roll_input).group(1))
        except ValueError:
            print("Invalid Entry, number of sides not found")
            return
    else:
        try:
            num_sides = int(roll_input.split()[-1])
        except ValueError or IndexError:
            print("Invalid entry, number of sides not found")
            return
    if re.search("[m](.+?)[ \a]", roll_input):
        try:
            modifier = int(re.search("[m](.+?)[ a]", roll_input).group(1))
        except ValueError:
            print("Invalid Entry, modifier not found")
            return
    else:
        modifier = 0
    if list(roll_input)[-1] == "a":
        advantage = True
        num_dice += 1
    elif list(roll_input)[-1] == "d":
        disadvantage = True
        num_dice += 1
    if num_dice == 1 and num_sides == 20:
        roll_d20 = random.randint(1, num_sides + 1)
        if roll_d20 == 1 or roll_d20 == 20:
            roll_total = roll_d20
            natural = True
        else:
            roll_total = roll_d20 + modifier
        return roll_total, natural
    rolls = []
    for dice in range(num_dice):
        rolls.append(random.randint(1, num_sides + 1))
    if advantage:
        rolls.remove(min(rolls))
    elif disadvantage:
        rolls.remove(max(rolls))
    roll_total = sum(rolls) + modifier
    return roll_total, natural


if __name__ == "__main__":
    roll(input("\nEnter roll details \"2d10m2(a)\"\n"))

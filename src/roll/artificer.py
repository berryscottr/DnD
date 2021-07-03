import sys

import artificer_vars as av
import roll as rl


def combat_selection():
    print("\nBonus Actions: ")
    for ba in av.bonus_actions:
        print(ba)
    print("\nCombat Actions: ")
    for ca in av.combat_actions:
        print(ca)
    print("\nReactions: ")
    for ra in av.reactions:
        print(ra)


def non_combat_selection():
    print("\nNon-Combat Actions: ")
    for nca in av.actions:
        print(nca)


if __name__ == "__main__":
    combat = input(
        "Combat - 1\nNon-Combat - 2\n"
    )
    if combat == "1":
        combat_selection()
    elif combat == "2":
        non_combat_selection()
    try:
        roll, natural = rl.roll(input("\nEnter roll details \"2d10m2(a)\"\n"))
    except TypeError:
        sys.exit()
    if natural:
        print("You rolled: \nNatural", roll)
    else:
        print("You rolled: \n", roll)

from random  import *

def rolling_dice(dice1, dice2, can_be_equal):
    while True:
        random1 = randint(1,dice1)
        random2 = randint(1,dice2)
        if random1 != random2 or can_be_equal:
            return random1, random2


print(rolling_dice(6,10,False))


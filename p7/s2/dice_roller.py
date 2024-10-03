# In this exercise you will write some functions which can be used in games that involve dice.

# Instead of normal dice this exercise specifies non-transitive dice. You can read up on these here or watch this video.

# You will use three dice:

# Die A has the sides 3, 3, 3, 3, 3, 6
# Die B has the sides 2, 2, 2, 5, 5, 5
# Die C has the sides 1, 4, 4, 4, 4, 4
# Please write a function named roll(die: str), which rolls the die specified by the argument. An example of how this should work:

# for i in range(20):
#     print(roll("A"), " ", end="")
# print()
# for i in range(20):
#     print(roll("B"), " ", end="")
# print()
# for i in range(20):
#     print(roll("C"), " ", end="")

# 3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  6  3  6  3
# 2  2  5  2  2  5  5  2  2  5  2  5  5  5  2  5  2  2  2  2
# 4  4  4  4  4  1  1  4  4  4  1  4  4  4  4  4  4  4  4  4

# Also write a function named play(die1: str, die2: str, times: int), which throws both dice as many times as specified by the third argument. The function should return a tuple. The first item should be the number of times die 1 won, the second the number of times die 2 won, and the third item should be the number of ties.

# result = play("A", "C", 1000)
# print(result)
# result = play("B", "B", 1000)
# print(result)

# (292, 708, 0)
# (249, 273, 478)

from random import choice
def roll(die: str):
    die_a = [3, 3, 3, 3, 3, 6]
    die_b = [2, 2, 2, 5, 5, 5]
    die_c = [1, 4, 4, 4, 4, 4]

    if die == "A":
        return choice(die_a)
    if die == "B":
        return choice(die_b)
    if die == "C":
        return choice(die_c)
    
def play(die1: str, die2: str, times: int):
    d1_wins = 0
    d2_wins = 0
    draws = 0

    for i in range(times):
        d1_roll = roll(die1)
        d2_roll = roll(die2)
        if d1_roll > d2_roll:
            d1_wins += 1
        elif d2_roll > d1_roll:
            d2_wins += 1
        else:
            draws += 1

    return d1_wins, d2_wins, draws
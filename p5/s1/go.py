# In a game of Go two players take turns to place black and white stones on a game board. The winner is the player who manages to encircle a bigger area on the board with their own game pieces.

# Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:

# 0: empty square
# 1: player 1 game piece
# 2: player 2 game piece
# The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.

# The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0.

def who_won(game_board: list) -> int:
    p1 = 0
    p2 = 0
    for row in game_board:
        for val in row:
            if val == 1:
                p1 += 1
            elif val == 2:
                p2 += 1

    if p1 == p2:
        return 0
    elif p1 > p2:
        return 1
    else:
        return 2
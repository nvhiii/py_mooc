class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here

# The exercise template contains the definition for a class named BallPlayer. It has the following public attributes:

# name
# shirt number number
# scored goals goals
# assists completed assists
# minutes played minutes
# Please implement the following functions. NB: each function has a different type of return value.

# Most goals
# Please write a function named most_goals which takes a list of ball players as its argument.

# The function should return the name of the player who scored the most goals, in string format.

# Most points
# Please write a function named most_points, which takes a list of ball players as its argument.

# The function should return a tuple containing the name and shirt number of the player who has scored the most points. The total number of points is the number of goals and the number of assists combined.

# Least minutes
# Please write a function named least_minutes, which takes a list of ball players as its argument.

# The function should return the BallPlayer object which has the smallest value of minutes played.

# You can test your functions with the following program:

# if __name__ == "__main__":
#     player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
#     player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
#     player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
#     player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
#     player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
#     team = [player1, player2, player3, player4, player5]
#     print(most_goals(team))
#     print(most_points(team))
#     print(least_minutes(team))

# This should print out:

# Archie Bonkers
# ('Cruella De Hill', 9)
# BallPlayer(name=Donald Quack, number=4, goals=3, assists=9, minutes=12)

def most_goals(ball_players: list):
    player = max(ball_players, key=lambda player: player.goals)
    return player.name

def most_points(ball_players: list):
    player = max(ball_players, key=lambda player: player.goals + player.passes) # i assume points are points + goals combined
    return player.name, player.number

def least_minutes(ball_players: list):
    return min(ball_players, key=lambda player: player.minutes)
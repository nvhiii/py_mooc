# Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.

# The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys.

# name
# director
# year
# runtime
# The values attached to these keys are given as arguments to the function.

# An example of its use:

# database = []
# add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(database)

# [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }

    database.append(movie)
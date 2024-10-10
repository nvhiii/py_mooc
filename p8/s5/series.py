# A class named Series
# Please write a class named Series with the following functionality:

# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# print(dexter)

# Dexter (8 seasons)
# genres: Crime, Drama, Mystery, Thriller
# no ratings

# The constructor should take the title, the number of seasons and a list of genres for the series as its arguments.

# Hint: whenever you need to produce a string from a list containing strings, with a separating character of your choice in between the entries, you can use the join method as follows:

# genre_list = ["Crime", "Drama", "Mystery", "Thriller"]
# genre_string = ", ".join(genre_list)
# print(genre_string)

# Crime, Drama, Mystery, Thriller

# Adding reviews
# Please implement the method rate(rating: int) which lets you add a rating between 0 and 5 to any series object. You will also need to adjust the __str__ method so that in case there are ratings, the method prints out the number of ratings added, and their average rounded to one decimal point.

# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# dexter.rate(4)
# dexter.rate(5)
# dexter.rate(5)
# dexter.rate(3)
# dexter.rate(0)
# print(dexter)

# Dexter (8 seasons)
# genres: Crime, Drama, Mystery, Thriller
# 5 ratings, average 3.4 points

# Searching for series
# Please implement these two functions which allow you to search through a list of series: minimum_grade(rating: float, series_list: list) and includes_genre(genre: str, series_list: list).

# Here is an example of how the new methods are used:

# s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# s1.rate(5)

# s2 = Series("South Park", 24, ["Animation", "Comedy"])
# s2.rate(3)

# s3 = Series("Friends", 10, ["Romance", "Comedy"])
# s3.rate(2)

# series_list = [s1, s2, s3]

# print("a minimum grade of 4.5:")
# for series in minimum_grade(4.5, series_list):
#     print(series.title)

# print("genre Comedy:")
# for series in includes_genre("Comedy", series_list):
#     print(series.title)

# a minimum rating of 4.5:
# Dexter
# genre Comedy:
# South Park
# Friends

# The code above and the automatic tests for this exercise assume your class contains an attribute title. If you used some other attribute name to refer to the name of the series, please change it before submitting.

class Series:

    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        if not self.ratings:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\nno ratings"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{len(self.ratings)} ratings, average {(sum(self.ratings)/len(self.ratings)):.1f} points"
    
    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)

def minimum_grade(grade: float, series_list: list):
    min_g = []
    for serie in series_list:
        if (sum(serie.ratings)/len(serie.ratings)) >= grade:
            min_g.append(serie)

    return min_g
    
def includes_genre(genre: str, series_list: list):
    inc_g = []
    for serie in series_list:
        if genre in serie.genres:
            inc_g.append(serie)

    return inc_g
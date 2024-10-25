# Write your solution here
import re

# Here are some exercises for familiarizing yourself with regular expression syntax.

# Days of the week
# Using a regular expression, please write a function named is_dotw(my_string: str). The function should return True if the string passed as an argument contains an abbreviation for a day of the week (Mon, Tue, Wed, Thu, Fri, Sat, Sun).

# Some examples of how the function should work:

# print(is_dotw("Mon"))
# print(is_dotw("Fri"))
# print(is_dotw("Tui"))

# True
# True
# False

# Check for vowels
# Please write a function named all_vowels(my_string: str) which uses a regular expression to check whether all characters in the given string are vowels.

# Some examples of how the function should work:

# print(all_vowels("eioueioieoieou"))
# print(all_vowels("autoooo"))

# True
# False

# Time of day
# Please write a function named time_of_day(my_string: str) which uses a regular expression to check whether a string in the format XX:YY:ZZ is a valid time in the 24-hour format, with two digits each for hours, minutes and seconds.

# Some examples of how the function should work:

# print(time_of_day("12:43:01"))
# print(time_of_day("AB:01:CD"))
# print(time_of_day("17:59:59"))
# print(time_of_day("33:66:77"))

# True
# False
# True
# False

def is_dotw(my_string: str):
    if re.search("(Mon|Tue|Wed|Thu|Fri|Sat|Sun)", my_string):
        return True
    return False

def all_vowels(my_string: str):
    for chara in my_string:
        if not re.search("[aeiou]", chara):
            return False
    return True

def time_of_day(my_string: str):
    # The correct regex pattern for time in HH:MM:SS format
    if re.match("^([01]\d|2[0-3]):[0-5]\d:[0-5]\d", my_string):
        return True
    return False
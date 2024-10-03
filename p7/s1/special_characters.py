# The Python module string contains some string constants, which define certain groups of characters. These include for example lowercase letters and punctuation characters. Please familiarize yourself with these constants, and then write a function named separate_characters(my_string: str). The function takes a string as its argument, and it should separate the characters in the string into three other strings, and return these in a tuple:

# The first string should contain the lowercase and uppercase ASCII letters (string constant ascii_letters)
# The second string should contain all punctuation characters defined by the string constant punctuation
# The third string should contain all the other characters (including whitespace)
# The characters should appear in the three strings in the same order as they appeared in the original string.

# An example of the function in action:

# parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
# print(parts[0])
# print(parts[1])
# print(parts[2])

# OlHeyaremltswrking
# !!!,?
# é  üäü ö

from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    letters = ""
    punc = ""
    rest = ""

    for char in my_string:
        if char in ascii_letters:
            letters += char
        elif char in punctuation:
            punc += char
        else:
            rest += char

    return letters, punc, rest
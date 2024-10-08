# Please write a module named string_helper, which contains the following functions:

# The function change_case(orig_string: str) creates and returns a new version of the parameter string. The lowercase letters in the original should be uppercase, and uppercase letters should be lowercase.

# The function split_in_half(orig_string: str) splits the parameter string in half, and returns the results in a tuple. If the original has an odd number of characters, the first half should be shorter.

# The function remove_special_characters(orig_string: str) returns a new version of the parameter string, with all special characters removed. Only lowercase and uppercase letters, numbers and spaces are allowed in the returned string.

# Some examples of how the module would be used:

# import string_helper

# my_string = "Well hello there!"

# print(string_helper.change_case(my_string))

# p1, p2 = string_helper.split_in_half(my_string)

# print(p1)
# print(p2)

# m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
# print(m2)

# wELL HELLO THERE!
# Well hel
# lo there!
# This is a test lets see how it goes11

from string import punctuation

def change_case(orig_string: str) -> str:
    # stores charas in list
    charas = list(orig_string) # cant split using empty delimiter
    for i, char in enumerate(charas):
        if char.isupper():
            charas[i] = char.lower()
        elif char.islower():
            charas[i] = char.upper()

    changed = "".join(charas)
    return changed

def split_in_half(orig_string: str) -> tuple:
    length = len(orig_string)
    half_len = length // 2
    return orig_string[:half_len+1] # How can i turn this into a tuple???

def remove_special_character(orig_string: str) -> str:
    specials = punctuation
    

    



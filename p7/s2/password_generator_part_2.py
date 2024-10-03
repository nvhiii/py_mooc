# Please write an improved version of your password generator. The function now takes three arguments:

# If the second argument is True, the generated password should also contain one or more numbers.
# If the third argument is True, the generated password should also contain one or more of these special characters: !?=+-()#.
# Despite these two additional arguments, the password should always contain at least one lowercase alphabet. You may assume the function will only be called with combinations of arguments that are possible to formulate into passwords following these rules. That is, the arguments will not specify e.g. a password of length 2 which contains both a number and a special characters, for then there would not be space for the mandatory lowercase letter.

# An example of how the function should work:

# for i in range(10):
#     print(generate_strong_password(8, True, True))

# 2?0n+u31
# u=m4nl94
# n#=i6r#(
# da9?zvm?
# 7h)!)g?!
# a=59x2n5
# (jr6n3b5
# 9n(4i+2!
# 32+qba#=
# n?b0a7ey

from random import choice, shuffle
from string import ascii_lowercase, digits

def generate_strong_password(length: int, numbers: bool, sp_charas: bool):
    strong_pwd = []
    lowercase = ascii_lowercase # all lower case charas
    nums = digits
    special_characters = "!?=+-()#"
    valid_selections = ""

    strong_pwd.append(choice(lowercase)) # chooses 1 random lowercase chara and appends to fulfill min of 1 lowercase chara
    valid_selections += lowercase

    if numbers == True:
        strong_pwd.append(choice(nums)) # fulfills 1 random num choice if nums bool is true
        valid_selections += nums
    if sp_charas == True:
        strong_pwd.append(choice(special_characters)) # fulfills 1 random special chara chocie if sp charas bool is true
        valid_selections += special_characters

    while len(strong_pwd) < length:
        strong_pwd.append(choice(valid_selections))

    # now since this is a list, must join
    pwd = "".join(strong_pwd)
    return pwd
    
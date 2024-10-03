# Please write a function which creates passwords of a desired length, consisting of lowercase characters a to z.

# An example of how the function should work:

# for i in range(10):
#     print(generate_password(8))

# lttehepy
# olsxttjl
# cbjncrzo
# dwxqjdgu
# gpfdcecs
# jabyvgar
# xnbbonbl
# ktmsjyww
# ejhprmel
# rjkoacib

from random import choice

def generate_password(length: int):
    pwd = ""
    num_range = list(range(97, 123)) # ascii for lowercase 123 for including last chara
    for i in range(length):
        draw = choice(num_range)
        chara = chr(draw)
        pwd += chara

    return pwd
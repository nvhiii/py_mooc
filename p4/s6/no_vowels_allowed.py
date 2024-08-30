# Please write a function named no_vowels, which takes a string argument. 
# The function returns a new string, which should be the same as the original 
# but with all vowels removed.

# You can assume the string will contain only characters from the lowercase 
# English alphabet a...z.

# An example of expected behaviour:

# my_string = "this is an example"
# print(no_vowels(my_string))

# ths s n xmpl

def no_vowels(ustr: str) -> str:
    # Replace each vowel with an empty string
    ustr = ustr.replace("a", "")
    ustr = ustr.replace("e", "")
    ustr = ustr.replace("i", "")
    ustr = ustr.replace("o", "")
    ustr = ustr.replace("u", "")

    return ustr
# The Python string method isupper() returns True if a 
# string consists of only uppercase characters.
#
# Please use the isupper method to write a function named no_shouting, which takes 
# a list of strings as an argument. The function returns a new 
# list, containing only those items from the original which do not 
# consist of solely uppercase characters.

def no_shouting(list):

    iterator = 0
    lowercase = []

    while iterator < len(list):

        if not (list[iterator].isupper()):
            lowercase.append(list[iterator])

        iterator += 1

    return lowercase

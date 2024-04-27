# Write your solution here
# Please write a function named length_of_longest, 
# which takes a list of strings as its argument. The 
# function returns the length of the longest string.

def length_of_longest(list):

    longest = ""
    for stringVal in list:

        # stores string, not len
        if len(stringVal) > len(longest):
            longest = stringVal

    return len(longest)
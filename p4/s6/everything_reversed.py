# Write your solution here
# Please write a function named everything_reversed, which takes 
# a list of strings as its argument. The function returns a new 
# list with all of the items on the original list reversed. 
# Also the order of items should be reversed on the new list.

def everything_reversed(list):

    reverseEverything = []
    lastIndex = len(list) - 1

    while lastIndex >= 0:

        # order of items swapped
        # now reverse each string
        reversedString = list[lastIndex][::-1]
        reverseEverything.append(reversedString)

        lastIndex -= 1

    return reverseEverything



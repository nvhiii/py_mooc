# Write your solution here
# Please write a function named all_the_longest, which 
# takes a list of strings as its argument. The function
# should return a new list containing the longest string in 
# the original list. If more than one are equally long, the 
# function should return all of the longest strings.

# The order of the strings in the returned list should 
# be the same as in the original.

def all_the_longest(list):

    maxString = ""
    newList = []
    iterator = 0

    while True:

        if iterator == len(list):
            break

            # set max string
        if (iterator == 0):
            maxString = list[0]
            newList.append(maxString)
            iterator += 1
            # update max
        elif (len(list[iterator]) > len(maxString)):
            newList.clear()
            maxString = list[iterator]
            newList.append(maxString)
            iterator += 1
        elif (len(list[iterator]) == len(maxString)):
            # if string lengths equal
            newList.append(list[iterator])
            iterator += 1
        else:
            iterator += 1

    return newList

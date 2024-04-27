# Write your solution here
# Please write a function named distinct_numbers, which 
# takes a list of integers as its argument. The function 
# returns a new list containing the numbers from the original 
# list in order of magnitude, and so that each distinct number 
# is present only once.

def distinct_numbers(list):

    newList = []

    for num in list:

        if num not in newList:

            newList.append(num)

    return sorted(newList)
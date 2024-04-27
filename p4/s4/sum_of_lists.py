# Write your solution here
# Please write a function named list_sum which 
# takes two lists of integers as arguments. The 
# function returns a new list which contains the sums 
# of the items at each index in the two original lists. 
# You may assume both lists have the same number of items.

def list_sum(list1, list2):

    newList = []

    for index in range(len(list1)):

        newList.append(list1[index] + list2[index])
             
    return newList
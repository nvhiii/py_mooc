# Write your solution here
# Please write a function named sum_of_positives, which 
# takes a list of integers as its argument. The function 
# returns the sum of the positive values in the list.

def sum_of_positives(list):

    sumPos = 0

    for num in list:
        if num > 0:
            sumPos += num
        
    return sumPos
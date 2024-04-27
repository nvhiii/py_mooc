# Write your solution here
# Please write a function named even_numbers, which takes 
# a list of integers as an argument. The function returns 
# a new list containing the even numbers from the original list.

def even_numbers(list):

    newList = []

    for num in list:
        if num % 2 == 0:
            newList.append(num)

    return newList

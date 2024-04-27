# Write your solution here
# Please write a function named shortest, which takes 
# a list of strings as its argument. The function returns 
# whichever of the strings is the shortest. If more than 
# one are equally short, the function can return any of the 
# shortest strings (there will be no such situation in the tests). 
# You may assume there will be no empty strings in the list.

def shortest(list):

    shortest = ""

    for index in range(len(list)):

        if index == 0:
            shortest = list[index]
        elif len(list[index]) < len(shortest):
            shortest = list[index]
    
    return shortest
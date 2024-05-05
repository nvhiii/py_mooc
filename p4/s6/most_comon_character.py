# Write your solution here
# Please write a function named most_common_character, which 
# takes a string argument. The function returns the character 
# which has the most occurrences within the string. If there are 
# many characters with equally many occurrences, the one which 
# appears first in the string should be returned.

def most_common_character(str):

    # var to hold the mode
    mostOccurence = ""
    mostValue = 0
    iterator = 0

    # find most occurences
    while iterator < len(str):
        
        if (iterator == 0):
            mostOccurence = str[0]
            mostValue = str.count(mostOccurence)
            iterator += 1
        elif (str.count(str[iterator]) > mostValue):
            mostOccurence = str[iterator]
            mostValue = str.count(mostOccurence)
            iterator += 1
        else:
            iterator += 1


    return mostOccurence
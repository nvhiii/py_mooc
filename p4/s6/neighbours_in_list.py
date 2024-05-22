# Given a list of integers, let's decide that two consecutive 
# items in the list are neighbours if their difference is 1. 
# So, items 1 and 2 would be neighbours, and so would items 56 and 55.

# Please write a function named longest_series_of_neighbours, 
# which looks for the longest series of neighbours within the list, 
# and returns its length.

# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of 
# neighbours would be [5, 4, 3, 4], with a length of 4.

def longest_series_of_neighbours(list):

    longest = 1
    nextResult = 1
    iterator = 0
    
    # start iterating list at 1, bc u wanna compare to num before
    for iterator in range(1, len(list)):

        # now start incrementing the resulting neighbors list length
        if (abs(list[iterator-1] - list[iterator]) == 1):
            nextResult += 1
        else:
            nextResult = 1

        # recursive call to assign longest 
        longest = max(longest, nextResult)

    return longest

if __name__ == "__main__":
    myList = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(myList))
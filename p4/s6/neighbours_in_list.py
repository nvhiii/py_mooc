# Given a list of integers, let's decide that two consecutive 
# items in the list are neighbours if their difference is 1. 
# So, items 1 and 2 would be neighbours, and so would items 56 and 55.

# Please write a function named longest_series_of_neighbours, 
# which looks for the longest series of neighbours within the list, 
# and returns its length.

# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of 
# neighbours would be [5, 4, 3, 4], with a length of 4.

def longest_series_of_neighbours(list):

    iterator = 0
    nextIndex = iterator + 1
    longestNeighbors = []


    while iterator < len(list):

        # currently, code is skipping over the index that are not within +-1 range, 
        # then appending longest.
        # need to add cond to just store the curr list, then check if new neighbors comes up.
        # if that set of neighbors is longer than one in memory, it overwrites.

        # first find 1st contiguous set of neighbors, set as longest, and store string,
        # next check if next string i
        if (list[iterator] - list[nextIndex] == 1 or list[nextIndex] - list[iterator] == 1):
            longestNeighbors.append(list[iterator])

        iterator += 1

    return longestNeighbors

if __name__ == "__main__":
    myList = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(myList))
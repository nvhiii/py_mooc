# Write your solution here
# Please write a function named range_of_list, which takes a 
# list of integers as an argument. The function returns the 
# difference between the smallest and the largest value in the list.

def range_of_list(list):

    smallest = min(list)
    largest = max(list)
    range = largest - smallest
    return range


# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
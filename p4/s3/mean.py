# Write your solution here
# Please write a function named mean, which takes a list of 
# integers as an argument. The function returns the arithmetic
# mean of the values in the list.

def mean(list):

    lenList = len(list)
    sumList = sum(list)
    mean = sumList / lenList
    return mean

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
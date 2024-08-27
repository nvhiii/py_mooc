# Please write a function named mean, which takes three integer arguments. 
# The function should print out the arithmetic mean of the three arguments

# Write your code here
def mean(x, y, z):
    sum = x + y + z
    print(f"{sum/3}")

# Testing the function
if __name__ == "__main__":
    mean(1, 2, 3)
# Please write a function named spruce, which takes one 
# argument. The function prints out the text a spruce!, and 
# the a spruce tree, the size of which is specified by the argument.

# Calling spruce(3) should print out

# a spruce!
#   *
#  ***
# *****
#   *

# Calling spruce(5) should print out

# a spruce!
#     *
#    ***
#   *****
#  *******
# *********
#     *

def spruce(dim):

    print("a spruce!")
    # 1 + 2n, where n is 0
    num = 0
    while num < dim:
        whitespace = dim - num - 1 # calculates amt of whitespace to left
        print((whitespace * " ") + (2 * num * "*") + "*") # prints asterik num times
        num += 1 # increment num of stars per row
    print(((dim - 1) * " ") + "*")

if __name__ == "__main__":
    num = int(input("Enter a dimension for the spruce: "))
    spruce(num)

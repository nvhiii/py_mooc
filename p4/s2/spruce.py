# Please write a function named spruce, which takes one argument.
# The function prints out the text a spruce!, and the a spruce 
# tree, the size of which is specified by the argument.

# Write your solution here
def spruce(num):
    i = 0
    MAX_WIDTH = 2 * num # we dont add the + 1 bc we added into the string directly
    print(f"a spruce!")
    # since the things iterate by 2n + 1
    while i < num:

        line = f"*" * 2 * i + (f"*" * 1)

        if i != num - 1:
            whitespace = (MAX_WIDTH - len(line)) // 2
            print((f" " * whitespace) + line)
        else:
            print(line)
        i += 1
    
    # print log of the tree
    ws2 = (MAX_WIDTH - 1) // 2
    print((f" " * ws2) + "*")
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
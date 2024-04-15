# Write your solution here

# Please write a function named line, which takes 
# two arguments: an integer and a string. The function
#  prints out a line of text, the length of which is 
# specified by the first argument. The character used to
# draw the line should be the first character in the 
# second argument. If the second argument is an empty 
# string, the line should consist of stars.

def line(num, str):
    
    if len(str) == 0:
        print(f"*" * num) # accounts for new lines, and better time efficiency
    else:
        print(f"{str[0]}" * num)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
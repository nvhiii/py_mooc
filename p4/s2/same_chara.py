# Please write a function named same_chars, which takes one
# string and two integers as arguments. The integers refer
# to indexes within the string. The function should return 
# True if the two characters at the indexes specified are the 
# same. Otherwise, and especially if either of the indexes 
# falls outside the scope of the string, the function returns False.

# Write your solution here
def same_chars(input_str, index1, index2):
    if index1 >= len(input_str) or index2 >= len(input_str):
        return False
    elif input_str[index1] != input_str[index2]:
        return False
    else:
        return True

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
# Please write a function named 
# print_many_times(text, times), which takes a 
# string and an integer as arguments. The integer 
# argument specifies how many times the string 
# argument should be printed out:

# Write your solution here
def print_many_times(str, times):
    i = 0
    while i < times:
        print(f"{str}")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)
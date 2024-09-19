# The file numbers.txt contains integer numbers, one number per line. The contents could look like this:

# 2
# 45
# 108
# 3
# -10
# 1100
# ...etc...

# Please write a function named largest, which reads the file and returns the largest number in the file.

# Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.

# NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors, take a look at the instructions following this exercise.

def largest():
    biggest = 0
    with open("numbers.txt") as new_file:
        for line in new_file:
            biggest = max(biggest, int(line))

    return biggest

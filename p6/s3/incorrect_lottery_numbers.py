# The file lottery_numbers.csv containts winning lottery numbers in the following format:

# week 1;5,7,11,13,23,24,30
# week 2;9,13,14,24,34,35,37
# ...etc...

# Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.

# The file has been corrupted. Lines in the file may contain the following kinds of errors (these exact lines may not be present in the file, but errors in a similar format will be):

# The week number is incorrect:

# week zzc;1,5,13,22,24,25,26

# One or more numbers are not correct:

# week 22;1,**,5,6,13,2b,34

# Too few numbers:

# week 13;4,6,17,19,24,33

# The numbers are too small or large:

# week 39;5,9,15,35,39,41,105

# The same number appears twice:

# week 41;5,12,3,35,12,14,36

# Please write a function named filter_incorrect(), which creates a file called correct_numbers.csv. The file should contain only those lines from the original file which are in the correct format.

def filter_incorrect():
    try:
        vals = []
        with open("lottery_numbers.csv") as lotto: # read + populate lotto dict
            for line in lotto:
                try:
                    line = line.strip()
                    parts = line.split(";") # week x; [list of nums]

                    week = parts[0].split(" ")
                    if len(week) != 2 or not week[1].isdigit():
                        raise ValueError("The week number is incorrect") # not a valid value
                    week_num = int(week[1])

                    nums = list(map(int, parts[1].split(",")))
                    if len(nums) != 7:
                        raise ValueError("There should be 7 numbers")
                    if max(nums) > 39 or min(nums) < 1:
                        raise ValueError("Numbers either too large or small")
                    if len(set(nums)) != len(nums):
                        raise ValueError("Repeated values in the 7 numbers")

                    vals.append(line) # since exceptionss take care of invalid input, this works fine

                except ValueError as e:
                    print(f"Skipping due to error: {e}")

        with open("correct_numbers.csv", "w") as correct:
            for item in vals:
                correct.write(f"{item}\n")
    except FileNotFoundError:
        pass
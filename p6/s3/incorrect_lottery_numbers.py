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
    # for every place you can possibly have a exception, use a try except
    try:
        weekly_lotto = []
        with open("lottery_numbers.csv") as lotto:
            for line in lotto:
                try:
                    line = line.strip()
                    parts = line.split(";")

                    # isolate the week x part
                    week_n_num = parts[0].split(" ")
                    if not week_n_num[1].isdigit():
                        raise ValueError("Week # is a not a valid number")
                    
                    # convert parts 1 into list of nums
                    nums = list(map(int, parts[1].split(",")))
                    if len(nums) != 7:
                        raise ValueError("Not enough weekly nums")
                    if min(nums) < 0 or max(nums) > 39:
                        raise ValueError("Numbers too big or small")
                    if len(set(nums)) != len(nums):
                        raise ValueError("Same values exist")
                    
                    weekly_lotto.append(line)

                    with open("correct_numbers.csv", "w") as correct:
                        for val in weekly_lotto:
                            correct.write(f"{val}\n")

                except ValueError as e:
                    print(f"Error raised by {e}") # this catches the error where the 
                    # list of nums may not have a num
                    continue

    except FileNotFoundError:
        pass

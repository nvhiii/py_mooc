# The file solutions.csv contains some solutions to mathematics problems:

# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...

# As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.

# Please write a function named filter_solutions() which

# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
# Using the example above, the file correct.csv would contain the lines

# Arto;2+5;7
# Pekka;3-2;1
# Pekka;5+5;10

# The other two would be in the file incorrect.csv.

# Please write the lines in the same order as they appear in the original file. Do not change the original file.

# NB: the function should have the exact same result, no matter how many times it is called. That is, it shouldn't matter if the function is called once

# filter_solutions()

# or multiple times in a row

# filter_solutions()
# filter_solutions()
# filter_solutions()
# filter_solutions()

# After the execution, the contents of the files correct.csv and incorrect.csv should be exactly the same in either case.

import os

def filter_solutions(file_name="solutions.csv"):

    # read and store
    solutions = []
    with open(file_name) as current_file:
        for line in current_file:
            line = line.strip()
            solution = line.split(";")
            solutions.append(solution)

    # now solutions contains lists of everyones solutions
    # now need to check if the correct.csv exists
    if not os.path.exists("correct.csv"):
        with open("correct.csv", "w") as corrects:
            pass

    if not os.path.exists("incorrect.csv"):
        with open("incorrec.csv", "w") as incorrects:
            pass

    with open("correct.csv", "w") as corr:
        for solu in solutions:
            if eval(solu[1]) == int(solu[2]):
                corr.write(f"{solu[0]};{solu[1]};{solu[2]}\n")

    with open("incorrect.csv", "w") as incorr:
        for solu in solutions:
            if eval(solu[1]) != int(solu[2]):
                incorr.write(f"{solu[0]};{solu[1]};{solu[2]}\n") 
                
    


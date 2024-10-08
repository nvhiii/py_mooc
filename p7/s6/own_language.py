# In this exercise you will write your own programming language executor. You can use any techniques and skills you have learnt on this course thus far.

# The programs will consist of rows, and each row will be in one of the following formats:

# PRINT [value]: prints the value
# MOV [variable] [value]: assigns the value to the variable
# ADD [variable] [value]: adds the value to the variable
# SUB [variable] [value]: subtracts the value from the variable
# MUL [variable] [value]: multiplies the variable by the value
# [location]:: names a line of code, so it can be jumped to from elsewhere
# JUMP [location]: jumps to the location specified
# IF [condition] JUMP [location]: if the condition is true, jump to the location specified
# END: finish execution
# The square brackets above are just a notation to signify operands; see below for usage examples.

# The program is executed line by line from the first line onwards. The execution ends when the executor comes across the command END, or when there are no more lines to execute.

# Each program has 26 pre-defined variables, named A to Z. Each variable has the value 0 when the program begins. The notation [variable] refers to one of these 26 variables.

# All the values processed by the program are integer numbers. The notation [value] refers either to a value stored in a variable, or an integer number typed in directly.

# The notation [location] refers to any name of a location which consists of lowercase letters a to z and/or numbers 0 to 9. Two different locations may not have the same name.

# The notation [condition] refers to any expression in the format [value] [comparison] [value], where [comparison] is one of the following operators: ==, !=, <, <=, > and >=.

# Please write a function named run(program), which takes a list containing the program commands as its argument. Each item on the list is a line of code in the program. The function should return a new list, which contains the results of the PRINT commands executed during the program's run.

# You may assume the function will only be given programs which are entirely in the correct format. You do not have to implement any input validation or error handling.

# This exercise is worth two points. You will receive one point if the commands PRINT, MOV, ADD, SUB, MUL and END are working correctly. You will receice another point if the rest of the commands, which are used to implement loops, also work.

# Below are some examples, which you may also use for testing. Example 1:
# program1 = []
# program1.append("MOV A 1")
# program1.append("MOV B 2")
# program1.append("PRINT A")
# program1.append("PRINT B")
# program1.append("ADD A B")
# program1.append("PRINT A")
# program1.append("END")
# result = run(program1)
# print(result)

# [1, 2, 3]

# Example 2:
# program2 = []
# program2.append("MOV A 1")
# program2.append("MOV B 10")
# program2.append("begin:")
# program2.append("IF A >= B JUMP quit")
# program2.append("PRINT A")
# program2.append("PRINT B")
# program2.append("ADD A 1")
# program2.append("SUB B 1")
# program2.append("JUMP begin")
# program2.append("quit:")
# program2.append("END")
# result = run(program2)
# print(result)
# [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

# Example 3 (factorial):
# program3 = []
# program3.append("MOV A 1")
# program3.append("MOV B 1")
# program3.append("begin:")
# program3.append("PRINT A")
# program3.append("ADD B 1")
# program3.append("MUL A B")
# program3.append("IF B <= 10 JUMP begin")
# program3.append("END")
# result = run(program3)
# print(result)
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

# Example 4 (prime numbers):
# program4 = []
# program4.append("MOV N 50")
# program4.append("PRINT 2")
# program4.append("MOV A 3")
# program4.append("begin:")
# program4.append("MOV B 2")
# program4.append("MOV Z 0")
# program4.append("test:")
# program4.append("MOV C B")
# program4.append("new:")
# program4.append("IF C == A JUMP error")
# program4.append("IF C > A JUMP over")
# program4.append("ADD C B")
# program4.append("JUMP new")
# program4.append("error:")
# program4.append("MOV Z 1")
# program4.append("JUMP over2")
# program4.append("over:")
# program4.append("ADD B 1")
# program4.append("IF B < A JUMP test")
# program4.append("over2:")
# program4.append("IF Z == 1 JUMP over3")
# program4.append("PRINT A")
# program4.append("over3:")
# program4.append("ADD A 1")
# program4.append("IF A <= N JUMP begin")
# result = run(program4)
# print(result)

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def run(program):
    # Initialize the 26 variables (A to Z)
    variables = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    labels = {}
    output = []

    # First pass: identify all labels and their positions
    for idx, line in enumerate(program):
        if line.endswith(":"):
            label = line[:-1]
            labels[label] = idx

    # Execute the program
    idx = 0
    while idx < len(program):
        parts = program[idx].split()

        # Handle each type of command
        if parts[0] == "PRINT":
            value = parts[1]
            if value.isalpha() and len(value) == 1:  # Variable
                output.append(variables[value])
            else:  # Integer value
                output.append(int(value))

        elif parts[0] == "MOV":
            var, value = parts[1], parts[2]
            variables[var] = variables[value] if value.isalpha() else int(value)

        elif parts[0] == "ADD":
            var, value = parts[1], parts[2]
            variables[var] += variables[value] if value.isalpha() else int(value)

        elif parts[0] == "SUB":
            var, value = parts[1], parts[2]
            variables[var] -= variables[value] if value.isalpha() else int(value)

        elif parts[0] == "MUL":
            var, value = parts[1], parts[2]
            variables[var] *= variables[value] if value.isalpha() else int(value)

        elif parts[0] == "JUMP":
            label = parts[1]
            idx = labels[label]
            continue

        elif parts[0] == "IF":
            condition = " ".join(parts[1:4])
            label = parts[4]
            if eval_condition(condition, variables):
                idx = labels[label]
                continue

        elif parts[0] == "END":
            break

        # Move to the next line
        idx += 1

    return output

def eval_condition(condition, variables):
    # Helper function to evaluate conditions
    left, op, right = condition.split()
    left_value = variables[left] if left.isalpha() else int(left)
    right_value = variables[right] if right.isalpha() else int(right)

    if op == "==":
        return left_value == right_value
    elif op == "!=":
        return left_value != right_value
    elif op == "<":
        return left_value < right_value
    elif op == "<=":
        return left_value <= right_value
    elif op == ">":
        return left_value > right_value
    elif op == ">=":
        return left_value >= right_value
    return False
# Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.

# A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

# An example of the function in action:

# k = factorials(5)
# print(k[1])
# print(k[3])
# print(k[5])

# 1
# 6
# 120

def factorials(n: int):
    facts = {}
    init = 1
    for idx in range(1, n+1):
        init *= idx
        facts[idx] = init

    return facts
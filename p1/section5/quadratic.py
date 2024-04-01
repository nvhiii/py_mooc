# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
val1 = float(input("Value of a: "))
val2 = float(input("Value of b: "))
val3 = float(input("Value of c: "))

discriminant = (val2**2) - (4 * val1 * val3)

x_pos = ((-1 * val2) + sqrt(discriminant))/(2 * val1)
x_neg = ((-1 * val2) - sqrt(discriminant))/(2 * val1)

print(f"The roots are {x_pos} and {x_neg}")
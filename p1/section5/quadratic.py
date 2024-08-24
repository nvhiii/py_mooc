from math import sqrt

a_value = float(input("Value of a: "))
b_value = float(input("Value of b: "))
c_value = float(input("Value of c: "))

x_pos = ((-1 * b_value) + sqrt((b_value**2) - (4 * a_value * c_value))) / (2 * a_value)
x_neg = ((-1 * b_value) - sqrt((b_value**2) - (4 * a_value * c_value))) / (2 * a_value)

print(f"The roots are {x_pos} and {x_neg}")
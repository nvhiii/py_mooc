# Write your solution here
float_num = float(input("Please type in a number: "))

# Assuming the number given by user is greater than zero
print(f"Integer part: {int(float_num)}")
print(f"Decimal part: {float_num - int(float_num)}")
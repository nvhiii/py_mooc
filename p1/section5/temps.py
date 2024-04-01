# Write your solution here
fahren = int(input("Please type in a temperature (F): "))
celcius = (fahren - 32) * (5/9)
print(f"{fahren} degrees Fahrenheit equals {celcius} degrees Celsius")
if celcius < 0:
    print(f"Brr! It's cold in here!")
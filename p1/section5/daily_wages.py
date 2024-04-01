# Write your solution here
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
if day != "Sunday":
    print(f"Daily wages: {wage * hours} euros")
if day == "Sunday":
    print(f"Daily wages: {(wage * 2) * hours} euros")
# Write your solution here
week_time = int(input("How many times a week do you eat at the student cafeteria?"))
st_lunch_price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? \n"))
print("Average food expenditure: ")
# 7 days in a week
print(f"Daily: {(week_time * st_lunch_price + groceries) / 7} euros")
print(f"Weekly: {week_time * st_lunch_price + groceries} euros")

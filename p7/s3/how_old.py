# Please write a program which asks the user for their date of birth, and then prints out how old the user was on the eve of the new millennium. The program should ask for the day, month and year separately, and print out the age in days. Please have a look at the examples below:
    
# Day: 10
# Month: 9
# Year: 1979
# You were 7417 days old on the eve of the new millennium.

# Day: 28
# Month: 3
# Year: 2005
# You weren't born yet on the eve of the new millennium.

# You may assume all day-month-year combinations given as an argument will be valid dates. That is, there will not be a date like February 31st.

from datetime import datetime

def how_old():
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))

    birthday = datetime(year, month, day)
    millenium = datetime(1999, 12, 31)
    if birthday > millenium:
        print("You weren't born yet on the eve of the new millennium.")
    else:
        age = millenium - birthday # time delta obj
        print(f"You were {age.days} days old on the eve of the new millennium.")

how_old()
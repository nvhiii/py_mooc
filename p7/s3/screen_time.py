# Please write a program for recording the amount of time the user has spent in front of a television, computer or mobile device screen over a specific period of time.

# The program should work as follows:

# Filename: late_june.txt
# Starting date: 24.6.2020
# How many days: 5
# Please type in screen time in minutes on each day (TV computer mobile):
# Screen time 24.06.2020: 60 120 0
# Screen time 25.06.2020: 0 0 0
# Screen time 26.06.2020: 180 0 0
# Screen time 27.06.2020: 25 240 15
# Screen time 28.06.2020: 45 90 5
# Data stored in file late_june.txt

# The user will input each day on a separate line, and the entries will contain three numbers separated by spaces, representing minutes.

# With the above input, the program should store the data in a file named late_june.txt. The contents should look like this:

# Time period: 24.06.2020-28.06.2020
# Total minutes: 780
# Average minutes: 156.0
# 24.06.2020: 60/120/0
# 25.06.2020: 0/0/0
# 26.06.2020: 180/0/0
# 27.06.2020: 25/240/15
# 28.06.2020: 45/90/5

from datetime import datetime, timedelta

def screen_time():
    # Get the file name from the user
    file = input("Filename: ")

    # Parse the starting date
    starting = input("Starting date (dd.mm.yyyy): ")
    try:
        formatted = datetime.strptime(starting, "%d.%m.%Y")
    except ValueError as e:
        print(f"Error: {e}")
        return  # Exit the function if the date is invalid

    # Get the number of days
    num_days = int(input("How many days: "))
    
    # Calculate the end date (include the last day)
    end_day = formatted + timedelta(days=num_days - 1)

    print("Please type in screen time in minutes on each day (TV computer mobile): ")

    one_day = timedelta(days=1)
    info = []
    start = formatted
    total_min = 0
    total_array = []

    while formatted <= end_day:  # Include the last day in the loop
        # Format date for the prompt
        screen_time_day = input(f"Screen time {formatted.strftime('%d.%m.%Y')}: ")
        
        # Clean up input and split into individual numbers
        screen_time_day = screen_time_day.strip()
        std_nums = list(map(int, screen_time_day.split(" ")))
        
        # Add up total minutes for each day
        total_array.append(sum(std_nums))
        total_min += sum(std_nums)

        # Format the screen time and add to info list
        screen_time_day = screen_time_day.replace(" ", "/")
        info.append(f"{formatted.strftime('%d.%m.%Y')}: {screen_time_day}")
        
        # Move to the next day
        formatted += one_day

    # Write the results to a file
    try:
        with open(file, "w") as new_file:
            new_file.write(f"Time period: {start.strftime('%d.%m.%Y')}-{end_day.strftime('%d.%m.%Y')}\n")
            new_file.write(f"Total minutes: {total_min}\n")
            new_file.write(f"Average minutes: {sum(total_array)/len(total_array):.1f}\n")
            for item in info:
                new_file.write(f"{item}\n")
    except FileNotFoundError:
        print(f"File {file} not found")
        return  # Exit if file couldn't be written

    print(f"Data stored in {file}")

# Call the function to test it
screen_time()

# The file start_times.csv contains individual start times for a programming exam, in the format name;hh:mm. An example:
    
# jarmo;09:00
# timo;18:42
# kalle;13:23

# Additionally, the file submissions.csv contains points and handin times for individual exercises. The format here is name;task;points;hh:mm. An example:
    
# jarmo;1;8;16:05
# timo;2;10;21:22
# jarmo;2;10;19:15
# jne...

# Your task is to find the students who spent over 3 hours on the exam tasks. That is, any student whose any task was handed in over 3 hours later than their exam start time is labelled a cheater. There may be more than one submission for the same task for each student. You may assume all times are within the same day.

# Please write a function named cheaters(), which returns a list containing the names of the students who cheated

import csv
from datetime import datetime, timedelta
def cheaters():
    cheats = []
    start = {}
    with open("start_times.csv", newline="") as csv_start:
        reader = csv.reader(csv_start, delimiter=";")
        for row in reader:
            start[row[0]] = datetime.strptime(row[1], "%H:%M")

    limit = timedelta(hours=3)

    end = {}
    with open("submissions.csv", newline="") as csv_end:
        reader2 = csv.reader(csv_end, delimiter=";")
        for row in reader2:
            name = row[0]
            handin_time = datetime.strptime(row[3], "%H:%M")

            if name in start:
                starting = start[name]
                if handin_time - starting > limit:
                    if name not in cheats:
                        cheats.append(name)

    return cheats

if __name__ == "__main__":
    cheaters()
        
    
# You have the CSV files from the previous exercise at your disposal again. Please write a function named final_points(), which returns the final exam points received by the students, in a dictionary format, following these criteria:

# If there are multiple submissions for the same task, the submission with the highest number of points is taken into account.
# If the submission was made over 3 hours after the start time, the submission is ignored.
# The tasks are numbered 1 to 8, and each submission is graded with 0 to 6 points.

# In the dicionary returned the key should be the name of the student, and the value the total points received by the student.

# Hint: nested dictionaries might be a good approach when processing the tasks and submission times of each student.
import csv
from datetime import datetime, timedelta
def final_points():

    start = {}
    stu_submissions = {}
    # first store start times in a dict
    with open("start_times.csv", newline="") as starter:
        data = csv.reader(starter, delimiter=";")
        for row in data:
            name = row[0]
            start_time = datetime.strptime(row[1], "%H:%M")
            start[name] = start_time

    time_limit = timedelta(hours=3)

    with open("submissions.csv", newline="") as submissions:
        info = csv.reader(submissions, delimiter=";") # this returns iterator which must be iterated via rows
        for row in info:
            name = row[0]
            task = int(row[1])
            points = int(row[2])
            hand_in = datetime.strptime(row[3], "%H:%M")

            # this block must be indented, bc if not, the variable val arent correct
            if name in start:
                starting = start[name]
                if hand_in - starting <= time_limit:
                    # now must initialize a nested dict for task + pts
                    if name not in stu_submissions:
                        stu_submissions[name] = {} # first dictionary
                    if task not in stu_submissions[name] or stu_submissions[name][task] < points: # in order to access the task, need to access name, then the nested task dict
                        stu_submissions[name][task] = points

    
    total_points = {}
    for k, v in stu_submissions.items():
        total_points[k] = sum(v.values())

    return total_points

if __name__ == "__main__":
    final_points()

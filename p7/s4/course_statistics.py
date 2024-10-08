# Retrieving the list of active courses
# At the address https://studies.cs.helsinki.fi/stats-mock/api/courses you will find basic information about some of the courses offered by the University of Helsinki Department of Computer Science, in JSON format.

# Please write a function named retrieve_all(), which retrieves the data of all the courses which are currently active (the field enabled has the value true). These should be returned as a list of tuples, in the following format:

# [
#     ('Full Stack Open 2020', 'ofs2019', 2020, 201),
#     ('DevOps with Docker 2019', 'docker2019', 2019, 36),
#     ('DevOps with Docker 2020', 'docker2020', 2020, 36),
#     ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)
# ]

# Each tuple contains the following fields from the original data:

# the name of the course: fullName
# name
# year
# the sum of the values listed in exercises
# NB: It is essential that you retrieve the data with the function urllib.request.urlopen, or the automated tests may not work correctly.

# NB2: The tests are designed so that they slightly modify the data retrieved from the internet, to make sure you do not hard-code your return values.

# NB3: Some Mac users have come across the following issue:

# File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/urllib/request.py", line 1353, in do_open
#     raise URLError(err)
# urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1124)>

# The solution depends on how Python is installed on your machine. In some cases executing the following in a terminal helps:

# cd "/Applications/Python 3.8/"
# sudo "./Install Certificates.command

# The path used in the cd command above depends on the version of Python you have installed. The path may also be, for example, "/Applications/Python 3.9/".

# Various solutions to the problem have been suggested.

# One trick some have found useful:

# import urllib.request
# import json
# import ssl # add this library to your import section

# def retrieve_all():
#     # add the following line to the beginning of all your functions
#     context = ssl._create_unverified_context()
#     # the rest of your function

# Another potential workaround:

# import urllib.request
# import certifi # add this library to your import section
# import json

# def retrieve_all():
#    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
#    # add a second argument to the function call
#    request = urllib.request.urlopen(address, cafile=certifi.where())
#    # the rest of your function

# Retrieving the data for a single course
# Each course also has its own URL, where more specific weekly data about the course is available. The URLs follow the format https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats, where you would replace the stars with the contents of the field name for the course you want to access.

# For example, the data for the course docker2019 is at the address https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2019/stats.

# Please write a function named retrieve_course(course_name: str), which returns statistics for the specified course, in dictionary format.

# For example, the function call retrieve_course("docker2019") would return a dictionary with the following contents:

# {
#     'weeks': 4,
#     'students': 220,
#     'hours': 5966,
#     'hours_average': 27,
#     'exercises': 4988,
#     'exercises_average': 22
# }

# The values in the dictionary are determined as follows:

# weeks: the number of JSON object literals retrieved
# students: the maximum number of students in all the weeks
# hours: the sum of all hour_total values in the different weeks
# hours_average: the hours value divided by the students value (rounded down to the closest integer value)
# exercises: the sum of all exercise_total values in the different weeks
# exercises_average: the exercises value divided by the students value (rounded down to the closest integer value)
# NB: See the notices in Part 1 of the exercise, as they apply here, too.

# NB2: The Python math module has a useful function for rounding down integers.

import json
import ssl
import urllib.request
import math
def retrieve_all():
    context = ssl._create_unverified_context()
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    with urllib.request.urlopen(url, context=context) as response:
        data = response.read().decode('utf-8')

    courses = json.loads(data)
    # now retrieve active courses
    active_courses = []
    for course in courses:
        if course["enabled"]: # dont need == True
            active_courses.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))

    return active_courses

def retrieve_course(course_name: str):
    context = ssl._create_unverified_context()
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    with urllib.request.urlopen(url, context=context) as response:
        data = response.read().decode('utf-8')

    course_data = json.loads(data)
    weeks = len(course_data)
    students = 0
    hours = 0
    exercises = 0
    for item in course_data:
        if int(item["students"  ]) > students:
            students = int(item["students"])
        hours += int(item["hours"])
        exercises += int(item["exercises"])

    hours_avg = math.floor(hours / students) if students > 0 else 0
    exercises_avg = math.floor(exercises / students) if students > 0 else 0

    return {
        'weeks': weeks,
        'students': students,
        'hours': hours,
        'hours_average': hours_avg,
        'exercises': exercises,
        'exercises_average': exercises_avg
    }

course = retrieve_course("docker2019")
print(course)

# Please write a program which asks for the number of students on 
# a course and the desired group size. The program will then print 
# out the number of groups formed from the students on the course. 
# If the division is not even, one of the groups may have fewer members 
# than specified.

# If you can't get your code working as expected, it is absolutely okay 
# to move on and come back to this exercise later. The topic of the next 
# section is conditional statements. This exercise can also be solved 
# using a conditional construction.

# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2

course_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

groups = course_students // group_size if course_students % group_size == 0 else course_students // group_size + 1

print(f"Number of groups formed: {groups}")
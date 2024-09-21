# This program works with two CSV files. One of them contains information about some students on a course:

# id;first;last
# 12345678;peter;pythons
# 12345687;jean;javanese
# 12345699;alice;adder

# The other contains the number of exercises each student has completed each week:

# id;e1;e2;e3;e4;e5;e6;e7
# 12345678;4;1;1;4;5;2;4
# 12345687;3;5;3;1;5;4;6
# 12345699;10;2;2;7;10;2;2

# As you can see above, both CSV files also have a header row, which tells you what each column contains.

# Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:
    
# Student information: students1.csv
# Exercises completed: exercises1.csv
# pekka peloton 21
# jaana javanainen 27
# liisa virtanen 35

# Hint: while testing your program, you may quickly run out of patience if you always have to type in the file names at the prompt. You might want to hard-code the user input, like so:

# if False:
#     # this is never executed
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"

# The actual functionality of the program is now "hidden" in the False branch of an if statement. It will never be executed.

# Now, if you want to quickly verify the program works correctly also with user input, you can just replace False with True:

# if True:
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # now this is the False branch, and is never executed
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"

# When you have verified your program works correctly, you can remove the if structure, keeping the commands asking for input.

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

# NB2: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.

def grade_courses(file_one: str, file_two: str, file_three: str):
    
    students = {}
    with open(file_one) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            students[parts[0]] = parts[1] + " " + parts[2]
    
    exercises = {}
    with open(file_two) as nf:
        for line in nf:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exercises[parts[0]] = sum(int(x) for x in parts[1:])

    exam_points = {}
    with open(file_three) as nf_2:
        for line in nf_2:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exam_points[parts[0]] = sum(int(x) for x in parts[1:])

    # calc the exam + exercise pts
    grades = {}
    exer_points = {}
    total_pts = {}
    for student_id in exercises:
        # must do special extraction on the exercise #
        exer_points[student_id] = int(exercises[student_id] // 4)
        exam_exer = int(exercises[student_id] // 4) + int(exam_points[student_id])
        total_pts[student_id] = exam_exer
        if exam_exer <= 14:
            grades[student_id] = 0
        elif exam_exer <= 17:
            grades[student_id] = 1
        elif exam_exer <= 20:
            grades[student_id] = 2
        elif exam_exer <= 23:
            grades[student_id] = 3
        elif exam_exer <= 27:
            grades[student_id] = 4
        else:
            grades[student_id] = 5

    # changed prints
    # Print header row
    print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exam_pts.':10}{'total_pts.':10}{'grade':10}")

    # Print each student's data
    for sid in students:
        print(f"{students[sid]:30}{exercises[sid]:<10}{exer_points[sid]:<10}{exam_points[sid]:<10}{total_pts[sid]:<10}{grades[sid]:<10}")

def main():
    if False:
        # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_points = input("Exam points: ")
    else:
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_points = "exam_points1.csv"
        grade_courses(student_info, exercise_data, exam_points)

if __name__ == "__main__":
    main()

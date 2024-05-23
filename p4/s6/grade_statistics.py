    # In this exercise you will write a program for printing out grade 
    # statistics for a university course.

    # The program asks the user for results from different students 
    # on the course. These include exam points and numbers of 
    # exercises completed. The program then prints out statistics based on the results.

    # Exam points are integers between 0 and 20. The number of 
    # exercises completed is an integer between 0 and 100.

    # The program keeps asking for input until the user types in 
    # an empty line. You may assume all lines contain valid input, 
    # which means that there are two integers on each line, or the line is empty.

    def grade_statistics():

        pts_sum = 0
        num_students = 0
        passed = 0
        zero = 0
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0

        while (True):
            
            points_exercises = input("Exam points and exercises completed: ")

            # break cond
            if (points_exercises == ""):
                break

            # now split this string, idx 0 is exam pts and 1 is exercises completed
            split_array = points_exercises.split(" ")

            # exam points can be max 20, right into sum
            exam_pts = int(split_array[0])
            # exercise points need to be converted further
            exercise_pts = int(split_array[1])
            
            if (exercise_pts / 100 == 1):
                exercise_pts = 10
            elif (exercise_pts / 100 >= 0.9):
                exercise_pts = 9
            elif (exercise_pts / 100 >= 0.8):
                exercise_pts = 8
            elif (exercise_pts / 100 >= 0.7):
                exercise_pts = 7
            elif (exercise_pts / 100 >= 0.6):
                exercise_pts = 6
            elif (exercise_pts / 100 >= 0.5):
                exercise_pts = 5
            elif (exercise_pts / 100 >= 0.4):
                exercise_pts = 4
            elif (exercise_pts / 100 >= 0.3):
                exercise_pts = 3
            elif (exercise_pts / 100 >= 0.2):
                exercise_pts = 2
            elif (exercise_pts / 100 >= 0.1):
                exercise_pts = 1
            else:
                exercise_pts = 0

            raw_grade = exam_pts + exercise_pts
            # this is running pts sum for all students
            pts_sum += raw_grade

            if (exam_pts < 10 or (raw_grade <= 14 and raw_grade >= 0)):
                grade = 0
                zero += 1
            elif (raw_grade <= 17 and raw_grade >= 15):
                grade = 1
                passed += 1
                one += 1
            elif (raw_grade <= 20 and raw_grade >= 18):
                grade = 2
                passed += 1
                two += 1 
            elif (raw_grade <= 23 and raw_grade >= 21):
                grade = 3
                passed += 1
                three += 1
            elif (raw_grade <= 27 and raw_grade >= 24):
                grade = 4
                passed += 1
                four += 1
            else:
                grade = 5
                passed += 1
                five += 1

            # iterate per student
            num_students += 1

        print("Statistics")
        print("Points average: " + (1.0 * pts_sum / num_students))
        print("Pass percentage: " + (1.0 * passed / num_students))
        print("Grade distribution:")
        print(f'\t5: {five*"*"}')
        print(f'\t5: {four*"*"}')
        print(f'\t5: {three*"*"}')
        print(f'\t5: {two*"*"}')
        print(f'\t5: {one*"*"}')
        print(f'\t5: {zero*"*"}')

    def main():
        grade_statistics()

    main()


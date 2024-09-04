def exercises_completed(exer_comp: int) -> int:
    # Convert exercises completed (0-100) into points (0-10)
    return exer_comp // 10

def summation(exam_points: list, exercise_points: list) -> list:
    grades = []
    for i in range(len(exam_points)):
        # Summing the exam points and exercise points
        total_points = exam_points[i] + exercise_points[i]
        if exam_points[i] < 10:  # Fails if exam points are less than 10
            grades.append(0)
        elif total_points >= 28:
            grades.append(5)
        elif total_points >= 24:
            grades.append(4)
        elif total_points >= 21:
            grades.append(3)
        elif total_points >= 18:
            grades.append(2)
        elif total_points >= 15:
            grades.append(1)
        else:
            grades.append(0)
    return grades

def main(): # define main
    exam_points = []
    exercise_points = []

    while True:
        val = input("Exam points and exercises completed: ")
        if not val:  # Exit the loop on empty input
            break
        split = val.split()
        exam_point = int(split[0])
        exercise_complete = int(split[1])

        exam_points.append(exam_point)
        exercise_points.append(exercises_completed(exercise_complete)) # converts and adds into one

    if len(exam_points) == 0:
        print("No data entered.")
        return

    grades = summation(exam_points, exercise_points) # returns new list of grades
    average_points = sum(exam_points) / len(exam_points)
    passed = len([grade for grade in grades if grade > 0]) # cool logic
    pass_percentage = (passed / len(grades)) * 100

    # Output statistics
    print("Statistics:")
    print(f"Points average: {average_points:.1f}") # formatting 
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1): # include step when iternating negatively
        print(f"  {i}: {'*' * grades.count(i)}")

if __name__ == "__main__": # call main
    main()

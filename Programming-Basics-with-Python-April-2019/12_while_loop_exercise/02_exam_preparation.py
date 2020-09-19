poor_grades_count = int(input())
command = input()
poor_grades = 0
last_problem = ""
problems_count = 0
grades_sum = 0

while command != "Enough" and poor_grades < poor_grades_count:
    problem_name = command
    grade = float(input())
    grades_sum += grade
    problems_count += 1
    last_problem = problem_name

    if grade <= 4.00:
        poor_grades += 1

    if poor_grades >= poor_grades_count:
        break

    command = input()

average_grade = grades_sum / problems_count

if poor_grades >= poor_grades_count:
    print(f"You need a break, {poor_grades} poor grades.")
else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem}")

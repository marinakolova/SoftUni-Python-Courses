days = int(input())
courses = int(input())
hours_per_course = int(input())

needed_hours = courses * hours_per_course
hours_for_learning = 0

for i in range(1, days + 1):
    if i % 2 == 0:
        hours_for_learning += 4
    elif i % 5 == 0:
        hours_for_learning += 2
    else:
        hours_for_learning += 1

if hours_for_learning >= needed_hours:
    hours_left = hours_for_learning - needed_hours
    print(f"You watched all the courses and are left with {hours_left} free hours")
else:
    complete_courses = 0
    while hours_for_learning >= hours_per_course:
        hours_for_learning -= hours_per_course
        complete_courses += 1
    count_uncomplete_courses = courses - complete_courses
    print(f"You need to complete {count_uncomplete_courses} more courses")

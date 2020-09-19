name = input()
counter = 1
sum = 0
repeats = 0
excluded = False

while counter <= 12 and excluded == False:
    grade = float(input())
    if grade >= 4.00:
        sum += grade
        counter += 1
    elif grade < 4.00:
        repeats += 1
        if repeats >= 2:
            excluded = True

if counter == 13:
    average = sum / (counter - 1)
    print(f"{name} graduated. Average grade: {average:.2f}")
elif counter < 13:
    print(f"{name} has been excluded at {counter} grade")

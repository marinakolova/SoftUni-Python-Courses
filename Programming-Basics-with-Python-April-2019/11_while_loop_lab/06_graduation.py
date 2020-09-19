name = input()
counter = 1
sum = 0

while counter <= 12:
    grade = float(input())
    if grade >= 4.00:
        sum += grade
        counter += 1

average = sum / (counter - 1)
print(f"{name} graduated. Average grade: {average:.2f}")



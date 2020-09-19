numbers = [float(number) for number in input().split(' ')]

while True:
    new_numbers = []
    found = False
    total_numbers = len(numbers)
    for index, number in enumerate(numbers):
        if index + 1 < total_numbers and numbers[index] == numbers[index + 1]:
            new_numbers.append(numbers[index] + numbers[index + 1])
            found = True
            numbers.remove(number)
            total_numbers = len(numbers)
        else:
            new_numbers.append(number)
    numbers = new_numbers[:]

    if not found:
        break

print(' '.join([str(n) for n in numbers]))
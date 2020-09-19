numbers = [int(number) for number in input().split(' ')]
occurrences = dict()

for number in numbers:
    occurrences[number] = occurrences.get(number, 0) + 1

for key in sorted(occurrences.keys()):
    print(f'{key} -> {occurrences[key]}')

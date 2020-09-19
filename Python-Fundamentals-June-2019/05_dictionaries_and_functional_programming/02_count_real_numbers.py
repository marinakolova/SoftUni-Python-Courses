numbers = [float(n) for n in input().split(' ')]
occurrences = dict()

for n in numbers:
    occurrences[n] = occurrences.get(n, 0) + 1

for key, value in sorted(occurrences.items(), key=lambda kv: kv[0]):
    print(f'{key} -> {value} times')
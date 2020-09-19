inp = input()
occurrences = dict()

for ch in inp:
    occurrences[ch] = occurrences.get(ch, 0) + 1

for key, value in occurrences.items():
    print(f'{key} -> {value}')
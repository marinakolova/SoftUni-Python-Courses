words = [word.lower() for word in input().split(' ')]
occurrences = dict()

for word in words:
    occurrences[word] = occurrences.get(word, 0) + 1

occurrences = [key for key, value in occurrences.items() if value % 2 == 1]
print(', '.join(occurrences))
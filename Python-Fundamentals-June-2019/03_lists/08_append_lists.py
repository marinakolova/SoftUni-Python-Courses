lists = [l for l in input().split('|')]
numbers = []
for l in reversed(lists):
    current_numbers = [n for n in l.split(' ') if n]
    numbers.extend(current_numbers)

print(' '.join(numbers))

numbers = [int(n) for n in input().split(' ')]
iterations = int(input())
largest_numbers = []

for _ in range(iterations):
    max_number = max(numbers)
    numbers.remove(max_number)
    largest_numbers.append(max_number)

print(' '.join([str(n) for n in reversed(sorted(largest_numbers))]))
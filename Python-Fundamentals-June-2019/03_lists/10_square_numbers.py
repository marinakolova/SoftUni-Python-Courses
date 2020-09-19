import math

numbers = input().split(' ')

square_roots = []

for n in numbers:
    n = int(n)
    if n > 0 and math.sqrt(n) == int(math.sqrt(n)):
        square_roots.append(n)

square_roots.sort()
square_roots.reverse()

print(' '.join([str(r) for r in square_roots]))

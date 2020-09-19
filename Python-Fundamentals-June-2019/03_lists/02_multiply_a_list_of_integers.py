numbers = [int(n) for n in input().split(' ')]
multiplier = int(input())
print(' '.join([str(n * multiplier) for n in numbers]))
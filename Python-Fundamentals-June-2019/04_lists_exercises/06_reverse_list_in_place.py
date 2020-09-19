numbers = [int(number) for number in input().split(' ')]
numbers.reverse()
print(' '.join([str(n) for n in numbers]))
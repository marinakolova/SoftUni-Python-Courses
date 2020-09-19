positive_numbers = [n for n in input().split(' ') if int(n) > 0]
if len(positive_numbers) > 0:
    print(' '.join(reversed(positive_numbers)))
else:
    print('empty')
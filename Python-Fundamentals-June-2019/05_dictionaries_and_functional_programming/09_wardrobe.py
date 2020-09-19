from collections import defaultdict

clothes = defaultdict(dict)

n = int(input())

for _ in range(n):
    color, dresses = input().split(' -> ')
    for dress in dresses.split(','):
        clothes[color][dress] = clothes[color].get(dress, 0) + 1

inp = input().strip().split(' ')
target_color = inp[0]
target_dress = ''.join(inp[1:])

for color, dresses in clothes.items():
    print(f'{color} clothes:')
    for dress, count in dresses.items():
        found = ''
        if target_color == color and target_dress == dress and count > 0:
            found = ' (found!)'
        print(f'* {dress} - {count}{found}')

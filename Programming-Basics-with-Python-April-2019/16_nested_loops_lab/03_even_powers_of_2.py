n = int(input())
current = 0

for i in range(0, n + 1, 2):
    current = 2 ** i
    print(current)

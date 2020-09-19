n = int(input())

p1 = []
p2 = []
p3 = []

for i in range(0, n):
    num = int(input())
    if num % 2 == 0:
        p1.append(num)
    if num % 3 == 0:
        p2.append(num)
    if num % 4 == 0:
        p3.append(num)

print(f"{(len(p1) / n * 100):.2f}%")
print(f"{(len(p2) / n * 100):.2f}%")
print(f"{(len(p3) / n * 100):.2f}%")

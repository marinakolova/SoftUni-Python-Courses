import math

l = float(input())
w = float(input())
a = float(input())

hall = (l * 100) * (w * 100)
wardrobe = (a * 100) * (a * 100)
bench = hall / 10

free_space = hall - wardrobe - bench

dancers_count = free_space / (40 + 7000)

print(f"{math.floor(dancers_count)}")

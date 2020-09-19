import math

figure = input()

if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == "circle":
    r = float(input())
    area = math.pi * r * r
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2

print(f"{area:.3f}")

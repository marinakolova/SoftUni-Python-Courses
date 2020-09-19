x = float(input())
y = float(input())
h = float(input())

front_wall = x * x - 1.2 * 2
back_wall = x * x
side_wall = x * y - 1.5 * 1.5

roof_side = x * y
roof_triangle = x * h / 2

green_area = front_wall + back_wall + 2 * side_wall
red_area = 2 * roof_side + 2 * roof_triangle

green_paint = green_area / 3.4
red_paint = red_area / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")

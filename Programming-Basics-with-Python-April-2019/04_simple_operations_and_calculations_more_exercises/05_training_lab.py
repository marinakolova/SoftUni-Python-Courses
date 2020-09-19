import math

length_in_meters = float(input())
width_in_meters = float(input())

seats_in_row = math.floor((width_in_meters * 100 - 100) / 70)
rows = math.floor((length_in_meters * 100) / 120)

total_seats_count = seats_in_row * rows - 3

print(total_seats_count)

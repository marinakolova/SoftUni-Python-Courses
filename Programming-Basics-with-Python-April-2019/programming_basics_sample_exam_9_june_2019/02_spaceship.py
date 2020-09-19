import math

ship_area = float(input()) * float(input()) * float(input())
astro_height = float(input())
room_area = (astro_height + 0.4) * 2 * 2
capacity = math.floor(ship_area / room_area)

if 3 <= capacity <= 10:
    print(f"The spacecraft holds {capacity} astronauts.")
elif capacity < 3:
    print("The spacecraft is too small.")
elif capacity > 10:
    print("The spacecraft is too big.")

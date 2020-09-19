volume = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

water_from_p1 = p1 * hours
water_from_p2 = p2 * hours
total_water = water_from_p1 + water_from_p2

if total_water <= volume:
    print(f"The pool is {(total_water / volume * 100):.2f}% full. "
          f"Pipe 1: {(water_from_p1 / total_water * 100):.2f}%. "
          f"Pipe 2: {(water_from_p2 / total_water * 100):.2f}%")
else:
    print(f"For {hours:.2f} hours the pool overflows with {(total_water - volume):.2f} liters.")

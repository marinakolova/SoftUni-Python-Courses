length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

volume = length * width * height

volume_in_liters = volume / 1000

water = volume_in_liters * (1 - percentage)

print(f"{water:.3f}")

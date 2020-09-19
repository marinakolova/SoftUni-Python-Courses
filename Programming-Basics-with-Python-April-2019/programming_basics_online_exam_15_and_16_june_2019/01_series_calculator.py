import math

name = input()
seasons = int(input())
episodes = int(input())
duration = float(input())

total_time = seasons * episodes * (duration * 1.2) + seasons * 10

print(f"Total time needed to watch the {name} series is {math.floor(total_time)} minutes.")

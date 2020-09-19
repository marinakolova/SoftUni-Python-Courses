import math

year = input()
p = int(input())
h = int(input())

games = (48 - h) * 3.0 / 4 + h + p * 2.0 / 3

if year == "leap":
    games += 0.15 * games

print(math.trunc(games))

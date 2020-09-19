import math

days = int(input())
food = int(input())

food_needed = (float(input()) + float(input()) + float(input()) / 1000) * days

if food >= food_needed:
    print(f"{math.floor(food - food_needed)} kilos of food left.")
else:
    print(f"{math.ceil(food_needed - food)} more kilos of food are needed.")

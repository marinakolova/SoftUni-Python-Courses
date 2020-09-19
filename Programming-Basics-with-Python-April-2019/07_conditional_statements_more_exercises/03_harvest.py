import math

square_meters = int(input())
grapes_per_meter = float(input())
liters_needed = int(input())
workers = int(input())

total_harvest = square_meters * grapes_per_meter
harvest = total_harvest * 0.4
wine_liters = harvest / 2.5

if liters_needed > wine_liters:
    print(f"It will be a tough winter! "
          f"More {math.floor(liters_needed - wine_liters)} liters wine needed.")
else:
    print(f"Good harvest this year! "
          f"Total wine: {math.floor(wine_liters)} liters.")
    print(f"{math.ceil(wine_liters - liters_needed)} liters left -> "
          f"{math.ceil((wine_liters - liters_needed) / workers)} liters per person.")

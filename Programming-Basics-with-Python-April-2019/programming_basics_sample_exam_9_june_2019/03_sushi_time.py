import math

sushi_zone = { "sashimi": 4.99, "maki": 5.29, "uramaki": 5.99, "temaki": 4.29 }
sushi_time = { "sashimi": 5.49, "maki": 4.69, "uramaki": 4.49, "temaki": 5.19 }
sushi_bar = { "sashimi": 5.25, "maki": 5.55, "uramaki": 6.25, "temaki": 4.75 }
asian_pub = { "sashimi": 4.50, "maki": 4.80, "uramaki": 5.50, "temaki": 5.50 }

sushi_type = input()
restaurant = input()
portions = int(input())
order_type = input()
total_price = 0

if restaurant == "Sushi Zone":
    total_price = sushi_zone[sushi_type] * portions
elif restaurant == "Sushi Time":
    total_price = sushi_time[sushi_type] * portions
elif restaurant == "Sushi Bar":
    total_price = sushi_bar[sushi_type] * portions
elif restaurant == "Asian Pub":
    total_price = asian_pub[sushi_type] * portions
else:
    print(f"{restaurant} is invalid restaurant!")
    exit()

if order_type == "Y":
    total_price += 0.2 * total_price

print(f"Total price: {math.ceil(total_price)} lv.")

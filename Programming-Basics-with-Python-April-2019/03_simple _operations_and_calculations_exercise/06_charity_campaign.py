days = int(input())
bakers = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cakes_value = cakes_count * 45
waffles_value = waffles_count * 5.80
pancakes_value = pancakes_count * 3.20

value_per_day = (cakes_value + waffles_value + pancakes_value) * bakers
value_total = value_per_day * days
value_for_charity = value_total - value_total / 8

print(f"{value_for_charity:.2f}")

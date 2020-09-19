days = int(input())
nights = days - 1
room_type = input()
rating = input()

price = 0

if room_type == "room for one person":
    price = nights * 18.00
elif room_type == "apartment":
    price = nights * 25.00
    if days < 10:
        price -= 0.30 * price
    elif 10 <= days <= 15:
        price -= 0.35 * price
    elif days > 15:
        price -= 0.50 * price
elif room_type == "president apartment":
    price = nights * 35.00
    if days < 10:
        price -= 0.10 * price
    elif 10 <= days <= 15:
        price -= 0.15 * price
    elif days > 15:
        price -= 0.20 * price

if rating == "positive":
    price += 0.25 * price
elif rating == "negative":
    price -= 0.10 * price

print(f"{price:.2f}")

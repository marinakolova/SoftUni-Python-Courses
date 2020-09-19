type_of_flowers = input()
count = int(input())
budget = int(input())

prices = {
    "Roses": 5.00,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3.00,
    "Gladiolus": 2.50
}

price = count * prices[type_of_flowers]

if type_of_flowers == "Roses" and count > 80:
    price -= 0.10 * price
elif type_of_flowers == "Dahlias" and count > 90:
    price -= 0.15 * price
elif type_of_flowers == "Tulips" and count > 80:
    price -= 0.15 * price
elif type_of_flowers == "Narcissus" and count < 120:
    price += 0.15 * price
elif type_of_flowers == "Gladiolus" and count < 80:
    price += 0.20 * price

money_left = budget - price
money_needed = price - budget

if money_left >= 0:
    print(f"Hey, you have a great garden with {count} {type_of_flowers} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_needed:.2f} leva more.")

budget = int(input())
season = input()
fishermen = int(input())

rent = {
    "Spring": 3000,
    "Summer": 4200,
    "Autumn": 4200,
    "Winter": 2600
}

price = rent[season]

if fishermen <= 6:
    price -= 0.10 * price
elif 7 <= fishermen <= 11:
    price -= 0.15 * price
elif fishermen >= 12:
    price -= 0.25 * price

if fishermen % 2 == 0 and season != "Autumn":
    price -= 0.05 * price

money_left = budget - price
money_needed = price - budget

if money_left >= 0:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_needed:.2f} leva.")

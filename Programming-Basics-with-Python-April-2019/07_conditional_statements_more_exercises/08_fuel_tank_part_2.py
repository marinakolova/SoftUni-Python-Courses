prices = {"Gas": 0.93, "Gasoline": 2.22, "Diesel": 2.33}
discounts = {"Gas": 0.08, "Gasoline": 0.18, "Diesel": 0.12}

fuel_type = input()
liters = float(input())
club_card = input()

total_price = 0

if club_card == "Yes":
    total_price = (prices[fuel_type] - discounts[fuel_type]) * liters
else:
    total_price = prices[fuel_type] * liters

if 20 <= liters <= 25:
    total_price -= (0.08 * total_price)
elif liters > 25:
    total_price -= (0.10 * total_price)

print(f"{total_price:.2f} lv.")

budget = float(input())
statists = int(input())
one_costume_price = float(input())

decor_price = 0.1 * budget
costumes_price = statists * one_costume_price

if statists >= 150:
    costumes_price -= 0.1 * costumes_price

total_price = decor_price + costumes_price
money_left = budget - total_price
money_needed = total_price - budget

if money_left < 0:
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

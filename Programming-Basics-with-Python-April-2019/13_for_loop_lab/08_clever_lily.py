age = int(input())
price = float(input())
toy_price = int(input())

toys_count = 0
money_given = 0
money_saved = 0

if age % 2 == 0:
    for i in range(0, int(age / 2)):
        toys_count += 1
        money_given += 10
        money_saved += money_given - 1
else:
    for i in range(0, int(age / 2)):
        toys_count += 1
        money_given += 10
        money_saved += money_given - 1
    toys_count += 1

money_from_toys = toys_count * toy_price
money = money_saved + money_from_toys

money_left = money - price
money_needed = price - money

if price <= money:
    print(f"Yes! {money_left:.2f}")
else:
    print(f"No! {money_needed:.2f}")

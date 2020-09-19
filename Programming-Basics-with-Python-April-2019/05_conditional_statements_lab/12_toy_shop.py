PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

trip_price = float(input())

puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

total_price = puzzles_count * PUZZLE_PRICE + \
              talking_dolls_count * TALKING_DOLL_PRICE + \
              teddy_bears_count * TEDDY_BEAR_PRICE + \
              minions_count * MINION_PRICE + \
              trucks_count * TRUCK_PRICE

if total_count >= 50:
    total_income = total_price - 0.25 * total_price
else:
    total_income = total_price

total_income_after_rent = total_income - 0.10 * total_income

money_left = total_income_after_rent - trip_price
money_needed = trip_price - total_income_after_rent

if money_left >= 0:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_needed:.2f} lv needed.")

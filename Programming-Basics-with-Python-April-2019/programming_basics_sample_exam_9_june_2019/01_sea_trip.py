days = 3
fuel_price = 420 / 100 * 7 * 1.85
food_price = float(input()) * days
souvenirs_price = float(input()) * days
hotel_price_per_day = float(input())
hotel_price = hotel_price_per_day * 0.9 \
              + hotel_price_per_day * 0.85 \
              + hotel_price_per_day * 0.8
total_money = fuel_price + food_price + souvenirs_price + hotel_price
print(f"Money needed: {total_money:.2f}")

whiskey_price = float(input())
beer_liters = float(input())
wine_liters = float(input())
rakia_liters = float(input())
whiskey_liters = float(input())

rakia_price = whiskey_price / 2
wine_price = rakia_price - (0.4 * rakia_price)
beer_price = rakia_price - (0.8 * rakia_price)

rakia_value = rakia_liters * rakia_price
wine_value = wine_liters * wine_price
beer_value = beer_liters * beer_price
whiskey_value = whiskey_liters * whiskey_price
total_value = rakia_value + wine_value + beer_value + whiskey_value

print(f"{total_value:.2f}")

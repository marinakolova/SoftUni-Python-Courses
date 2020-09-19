tables_count = int(input())
tables_length = float(input())
tables_width = float(input())

covers_area = tables_count * (tables_length + 2 * 0.30) * (tables_width + 2 * 0.30)
squares_area = tables_count * (tables_length / 2) * (tables_length / 2)

price_USD = covers_area * 7 + squares_area * 9
price_BGN = price_USD * 1.85

print(f"{price_USD:.2f} USD")
print(f"{price_BGN:.2f} BGN")

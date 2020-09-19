import math

budget = (int(input()) * 3.25 \
         + int(input()) * 4 \
         + int(input()) * 3.50 \
         + int(input()) * 8) * 0.95
gift_price = float(input())

if budget >= gift_price:
    print(f"She is left with {math.floor(budget - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - budget)} leva.")

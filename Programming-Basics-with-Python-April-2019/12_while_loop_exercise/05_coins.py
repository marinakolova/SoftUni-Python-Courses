change = int(float(input()) * 100)
coins = 0

for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
    if change == 0:
        break
    while change >= coin:
        change -= coin
        coins += 1

print(coins)

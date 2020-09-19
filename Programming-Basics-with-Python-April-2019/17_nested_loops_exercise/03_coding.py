n = input()

for num in reversed(n):
    num = int(num)
    for pos in range(num):
        if num != 0:
            symbol = chr(num + 33)
            print(symbol, end="")
    if num == 0:
        print("ZERO")
    else:
        print()

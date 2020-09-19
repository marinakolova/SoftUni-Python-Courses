a1 = int(input())
a2 = int(input())
n = int(input())

for i in range(a1, a2):
    for j in range(1, n):
        for k in range(1, int(n / 2)):
            symbol_1 = chr(i)
            symbol_2 = j
            symbol_3 = k
            symbol_4 = i

            if i % 2 != 0 and (symbol_2 + symbol_3 + symbol_4) % 2 != 0:
                print(f"{symbol_1}-{symbol_2}{symbol_3}{symbol_4}")

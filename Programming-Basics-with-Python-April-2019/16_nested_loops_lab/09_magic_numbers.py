n = int(input())

for x1 in range(1, 10):
    for x2 in range(1, 10):
        for x3 in range(1, 10):
            for x4 in range(1, 10):
                for x5 in range(1, 10):
                    for x6 in range(1, 10):
                        product = x1 * x2 * x3 * x4 * x5 * x6
                        if product == n:
                            print(f"{x1}{x2}{x3}{x4}{x5}{x6}", end=" ")

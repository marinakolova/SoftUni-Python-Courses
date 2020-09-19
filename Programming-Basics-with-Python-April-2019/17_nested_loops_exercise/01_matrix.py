a = int(input())
b = int(input())
c = int(input())
d = int(input())

for first_row_first_num in range(a, b + 1):
    for first_row_second_num in range(a, b + 1):
        for second_row_first_num in range(c, d + 1):
            for second_row_second_num in range(c, d + 1):
                if (first_row_first_num + second_row_second_num) == (first_row_second_num + second_row_first_num) \
                        and first_row_first_num != first_row_second_num \
                        and second_row_first_num != second_row_second_num:
                    print(f"{first_row_first_num}{first_row_second_num}")
                    print(f"{second_row_first_num}{second_row_second_num}\n")

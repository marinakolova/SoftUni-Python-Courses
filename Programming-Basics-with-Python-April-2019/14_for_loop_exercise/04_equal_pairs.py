n = int(input())

sum = 0
prev_sum = 0
diff = 0
max_diff = 0

for i in range (1, n + 1):
    first_num = int(input())
    second_num = int(input())
    sum = first_num + second_num

    if i > 1:
        diff = abs(sum - prev_sum)
        if diff > max_diff:
            max_diff = diff

    prev_sum = sum
    sum = 0

if max_diff == 0:
    print(f"Yes, value={prev_sum}")
else:
    print(f"No, maxdiff={max_diff}")

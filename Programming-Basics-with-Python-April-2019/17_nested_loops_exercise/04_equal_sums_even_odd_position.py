first_num = int(input())
second_num = int(input())

for num in range(first_num, second_num + 1):
    num = str(num)
    counter = 1
    even_sum = 0
    odd_sum = 0

    for digit in num:
        digit = int(digit)
        if counter % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        counter += 1

    if even_sum == odd_sum:
        print(num, end=" ")

print()

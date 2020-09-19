n = int(input())
odd_sum = 0
even_sum = 0

if n % 2 == 0:
    for i in range(0, int(n / 2)):
        odd_num = int(input())
        odd_sum += odd_num
        even_num = int(input())
        even_sum += even_num
else:
    for i in range(0, int(n / 2)):
        odd_num = int(input())
        odd_sum += odd_num
        even_num = int(input())
        even_sum += even_num
    last_odd_num = int(input())
    odd_sum += last_odd_num

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum)}")

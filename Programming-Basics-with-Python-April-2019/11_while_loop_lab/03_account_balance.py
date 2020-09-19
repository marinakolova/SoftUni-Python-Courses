count = int(input())
total_money = 0
input_money = 0

while count > 0:
    input_money = float(input())
    if input_money < 0:
        print("Invalid operation!")
        break
    total_money += input_money
    print(f"Increase: {input_money:.2f}")
    count -= 1

print(f"Total: {total_money:.2f}")

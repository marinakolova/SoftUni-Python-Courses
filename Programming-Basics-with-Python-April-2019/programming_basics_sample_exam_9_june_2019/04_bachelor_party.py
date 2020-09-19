singer_price = int(input())
guests = 0
income = 0

command = input()

while command != "The restaurant is full":
    group = int(command)
    guests += group
    if group < 5:
        income += group * 100
    else:
        income += group * 70

    command = input()

money_left = income - singer_price

if money_left < 0:
    print(f"You have {guests} guests and {income} leva income, but no singer.")
else:
    print(f"You have {guests} guests and {money_left} leva left.")

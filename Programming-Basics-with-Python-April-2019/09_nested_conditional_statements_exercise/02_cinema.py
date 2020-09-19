type = input()
r = int(input())
c = int(input())

capacity = r * c
income = 0

if type == "Premiere":
    income = capacity * 12.00
elif type == "Normal":
    income = capacity * 7.50
elif type == "Discount":
    income = capacity * 5.00

print(f"{income:.2f}")

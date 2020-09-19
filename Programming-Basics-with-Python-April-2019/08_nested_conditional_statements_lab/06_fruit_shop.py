working_days_prices = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

weekend_prices = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

fruit = input()
day = input()
quantity = float(input())
price = 0

if day in working_days:
    if fruit in working_days_prices:
        price = quantity * working_days_prices[fruit]
    else:
        print("error")
        exit()
elif day in weekend:
    if fruit in weekend_prices:
        price = quantity * weekend_prices[fruit]
    else:
        print("error")
        exit()
else:
    print("error")
    exit()

print(f"{price:.2f}")

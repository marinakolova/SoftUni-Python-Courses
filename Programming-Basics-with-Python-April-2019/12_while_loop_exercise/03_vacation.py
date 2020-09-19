trip_price = float(input())
money_balance = float(input())
spend_times = 0
days_count = 0

while spend_times < 5 and money_balance < trip_price:
    action = input()
    sum = float(input())
    days_count += 1

    if action == "spend":
        spend_times += 1
        if sum >= money_balance:
            money_balance = 0
        else:
            money_balance -= sum
    elif action == "save":
        spend_times = 0
        money_balance += sum

if spend_times >= 5:
    print(f"You can't save the money.")
    print(f"{days_count}")
elif money_balance >= trip_price:
    print(f"You saved the money for {days_count} days.")

fuel = input()
liters = float(input())

if fuel not in ["Diesel", "Gasoline", "Gas"]:
    print("Invalid fuel!")
    exit()

if liters >= 25:
    print(f"You have enough {fuel.lower()}.")
else:
    print(f"Fill your tank with {fuel.lower()}!")

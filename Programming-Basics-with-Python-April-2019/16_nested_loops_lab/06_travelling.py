destination = input()

while destination != "End":
    needed_money = float(input())
    saved_money = 0

    while saved_money < needed_money:
        saved_money += float(input())

    print(f"Going to {destination}!")
    destination = input()

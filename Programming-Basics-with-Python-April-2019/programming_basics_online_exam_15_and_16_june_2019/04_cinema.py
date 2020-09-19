capacity = int(input())
income = 0

command = input()

while command != "Movie time!":
    group_count = int(command)

    if group_count > capacity:
        print("The cinema is full.")
        print(f"Cinema income - {income} lv.")
        exit()

    capacity -= group_count
    group_tax = group_count * 5
    if group_count % 3 == 0:
        group_tax -= 5
    income += group_tax

    command = input()

print(f"There are {capacity} seats left in the cinema.")
print(f"Cinema income - {income} lv.")

atomic_numbers = list(map(int, input().split(", ")))

used_indices = []
total_found_compounds = 0

remaining_elements = []
for num in atomic_numbers:
    remaining_elements.append(num)

while True:
    command = input()
    if command == "end":
        break

    indices = list(map(int, command.split("-")))
    formed_compound = []
    is_valid = True

    for index in indices:
        if not is_valid:
            continue
        if index < 0 or index >= len(atomic_numbers):
            print("Invalid indices")
            is_valid = False
            continue
        elif index in used_indices:
            print(f"Index {index} already taken")
            is_valid = False
            continue

    if is_valid:
        for index in indices:
            formed_compound.append(atomic_numbers[index])
            used_indices.append(index)
        total_found_compounds += 1
        print(f"Found compound: {formed_compound}")

for ind in sorted(used_indices, reverse=True):
    remaining_elements.pop(ind)

print(f"Total compounds: {total_found_compounds}")
print(f"Elements left: {remaining_elements}")

target_key = input()
target_value = input()
n = int(input())

for _ in range(n):
    line = input()
    line_parts = line.split(' => ')
    if len(line_parts) != 2:
        continue

    key = line_parts[0]
    values = [v.strip() for v in line_parts[1].split(';')]
    if target_key.lower() in key.lower():
        print(f'{key}:')
        for v in [v for v in values if target_value.lower() in v.lower()]:
            print(f'-{v}')
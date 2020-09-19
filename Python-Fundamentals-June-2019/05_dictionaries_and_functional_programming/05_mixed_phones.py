phones = dict()

while True:
    inp = input()
    if inp == 'Over':
        break

    name, number = inp.split(' : ')
    if name.isdigit():
        phones[number] = name
    else:
        phones[name] = number

for name, number in sorted(phones.items(), key=lambda kv: kv[0]):
    print(f'{name} -> {number}')
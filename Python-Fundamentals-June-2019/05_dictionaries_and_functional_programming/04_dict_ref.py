names = dict()

while True:
    inp = input()
    if inp == 'end':
        break

    name, value = inp.split(' = ')
    if value in names:
        names[name] = names[value]
    elif value.isdigit():
        names[name] = int(value)

for key, value in names.items():
    print(f'{key} === {value}')
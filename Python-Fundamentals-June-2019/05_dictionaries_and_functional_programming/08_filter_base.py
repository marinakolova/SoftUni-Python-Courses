def print_employee(employee_name, val, key):
    print(f'Name: {employee_name}')
    print(f'{key}: {val}')
    print('=' * 20)


ages, salaries, positions = {}, {}, {}

while True:
    inp = input()
    if inp == 'filter base':
        break

    inp = inp.split(' -> ')
    if len(inp) != 2:
        continue

    name, value = inp
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
            if int(value) == float(value):
                value = int(value)
        except ValueError:
            pass

    if type(value) == int:
        ages[name] = value
    elif type(value) == float:
        salaries[name] = value
    else:
        positions[name] = value

filter_base = input()
collection = ages if filter_base == 'Age' else salaries if filter_base == 'Salary' else positions
for name, value in collection.items():
    print_employee(name, value, filter_base)

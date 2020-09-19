result = dict()

while True:
    inp = input()
    if inp == 'end':
        break

    key, values = inp.split(' -> ')
    values = values.split(', ')
    if values[0].isdigit():
        if key in result:
            for v in values:
                result[key].append(int(v))
        else:
            result[key] = [int(v) for v in values]
    elif values[0] in result:
        if key in result:
            for v in result[values[0]]:
                result[key].append(int(v))
        else:
            result[key] = []
            for v in result[values[0]]:
                result[key].append(int(v))

for k, v in result.items():
    print(f'{k} === ' + ', '.join([str(n) for n in v]))

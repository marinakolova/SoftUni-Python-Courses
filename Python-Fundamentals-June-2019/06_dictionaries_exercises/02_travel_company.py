cities = dict()
 
while True:
    inp = input()
    if inp == 'ready':
        break
 
    city, transports = inp.split(':')
    for transport in transports.split(','):
        transport_type, capacity = transport.split('-')
        if city not in cities:
            cities[city] = dict()
        cities[city][transport_type] = int(capacity)
 
while True:
    inp = input()
    if inp == 'travel time!':
        break
 
    city, people = inp.split(' ')
    people = int(people)
    capacity_for_city = sum(cities[city].values())
    if capacity_for_city >= people:
        print(f'{city} -> all {people} accommodated')
    else:
        print(f'{city} -> all except {people - capacity_for_city} accommodated')

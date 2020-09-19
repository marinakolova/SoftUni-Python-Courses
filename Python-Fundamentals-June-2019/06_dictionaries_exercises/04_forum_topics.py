topics = dict()

while True:
    inp = input()
    if inp == 'filter':
        break

    topic, tags = inp.split(' -> ')
    if topic not in topics:
        topics[topic] = []

    for tag in tags.split(', '):
        if tag not in topics[topic]:
            topics[topic].append(tag)


target_tags = input().split(', ')

for topic, tags in topics.items():
    contains_all = True
    for t in target_tags:
        if t not in tags:
            contains_all = False
            break

    if contains_all:
        print_line = f'{topic} | '
        for t in tags:
            print_line += f'#{t}, '

        print(print_line.strip(', '))

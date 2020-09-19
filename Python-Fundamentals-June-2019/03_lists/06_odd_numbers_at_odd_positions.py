result = [f'Index {index} -> {number}'
          for index, number in enumerate(input().split(' '))
          if index % 2 == 1 and int(number) % 2 == 1]
for r in result:
    print(r)

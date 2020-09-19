numbers_list = list(map(int, input().split()))

data = input()
counter = 0

while not data == "exhausted":
    manipulated_nums_list = []
    data_list = data.split()
    command = data_list[0]

    if command == 'set':
        if len(set(numbers_list)) == len(numbers_list):
            print("It is a set")
        else:
            manipulated_nums_list = list(sorted(set(numbers_list), key=numbers_list.index))
    elif command == 'filter':
        even_or_odd = data_list[1]
        if even_or_odd == 'even':
            manipulated_nums_list = [num for num in numbers_list if num % 2 == 0]
        elif even_or_odd == 'odd':
            manipulated_nums_list = [num for num in numbers_list if num % 2 == 1]

    elif command == 'multiply':
        number = int(data_list[1])
        manipulated_nums_list = list(map(lambda el: el * number, numbers_list))
    elif command == 'divide':
        number = int(data_list[1])
        if number == 0:
            print('ZeroDivisionError caught')
        else:
            manipulated_nums_list = list(map(lambda el: el / number, numbers_list))
    elif command == 'slice':
        n = int(data_list[1])
        m = int(data_list[2])

        if (n >= 0 and n < len(numbers_list) and m >= 0 and m < len(numbers_list)):
            manipulated_nums_list = numbers_list[n:m + 1]
        else:
            print("IndexError caught")
    elif command == 'sort':
        manipulated_nums_list = list(sorted(numbers_list))
    elif command == 'reverse':
        manipulated_nums_list = list(reversed(numbers_list))

    if len(manipulated_nums_list) > 0:
        print(manipulated_nums_list)

    counter += 1
    data = input()

print(f"I beat It for {counter} rounds!")

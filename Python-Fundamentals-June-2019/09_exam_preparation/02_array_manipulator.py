array = input().split(" ")
array = list(map(int, array))

while True:
    command = input().split(" ")

    if command[0] == "end":
        break

    elif command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(array):
            print("Invalid index")
            continue
        array = array[index + 1:] + array[:index + 1]

    elif command[0] == "max":

        if command[1] == "even":
            even_numbers = list(filter(lambda n: n % 2 == 0, array))
            if not even_numbers:
                print("No matches")
                continue
            max_even_num = max(even_numbers)
            # print(array.index(max_even_num))
            index_to_print = len(array) - 1 - array[::-1].index(max_even_num)
            print(index_to_print)

        elif command[1] == "odd":
            odd_numbers = list(filter(lambda n: n % 2 != 0, array))
            if not odd_numbers:
                print("No matches")
                continue
            max_odd_num = max(odd_numbers)
            # print(array.index(max_odd_num))
            index_to_print = len(array) - 1 - array[::-1].index(max_odd_num)
            print(index_to_print)

    elif command[0] == "min":

        if command[1] == "even":
            even_numbers = list(filter(lambda n: n % 2 == 0, array))
            if not even_numbers:
                print("No matches")
                continue
            min_even_num = min(even_numbers)
            # print(array.index(max_even_num))
            index_to_print = len(array) - 1 - array[::-1].index(min_even_num)
            print(index_to_print)

        elif command[1] == "odd":
            odd_numbers = list(filter(lambda n: n % 2 != 0, array))
            if not odd_numbers:
                print("No matches")
                continue
            min_odd_num = min(odd_numbers)
            # print(array.index(max_odd_num))
            index_to_print = len(array) - 1 - array[::-1].index(min_odd_num)
            print(index_to_print)

    elif command[0] == "first":
        count = int(command[1])
        if count > len(array):
            print("Invalid count")
            continue

        if command[2] == "even":
            even_numbers = list(filter(lambda n: n % 2 == 0, array))
            if not even_numbers:
                print("[]")
                continue
            if len(even_numbers) > count:
                print(even_numbers[:count])
            else:
                print(even_numbers)

        elif command[2] == "odd":
            odd_numbers = list(filter(lambda n: n % 2 != 0, array))
            if not odd_numbers:
                print("[]")
                continue
            if len(odd_numbers) > count:
                print(odd_numbers[:count])
            else:
                print(odd_numbers)

    elif command[0] == "last":
        count = int(command[1])
        if count > len(array):
            print("Invalid count")
            continue

        if command[2] == "even":
            even_numbers = list(filter(lambda n: n % 2 == 0, array))
            if not even_numbers:
                print("[]")
                continue
            if len(even_numbers) > count:
                print(even_numbers[-count:])
            else:
                print(even_numbers)

        elif command[2] == "odd":
            odd_numbers = list(filter(lambda n: n % 2 != 0, array))
            if not odd_numbers:
                print("[]")
                continue
            if len(odd_numbers) > count:
                print(odd_numbers[-count:])
            else:
                print(odd_numbers)

print(array)

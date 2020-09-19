while True:
    inp = input()
    if inp == "stop playing":
        break

    elements = list(map(int, filter(None, inp.split(" "))))
    are_unique = len(elements) == len(set(elements))

    if are_unique:
        for i in range(0, len(elements)):
            if elements[i] % 2 == 0:
                elements[i] += 2
        list_to_print = ",".join(map(str, sorted(elements)))
        print(f"Unique list: {list_to_print}")
        sum_to_print = sum(elements) / len(elements)
        print(f"Output: {sum_to_print:.2f}")

    else:
        for i in range(0, len(elements)):
            if elements[i] % 2 != 0:
                elements[i] += 3
        list_to_print = ":".join(map(str, sorted(elements)))
        print(f"Non-unique list: {list_to_print}")
        sum_to_print = sum(elements) / len(elements)
        print(f"Output: {sum_to_print:.2f}")

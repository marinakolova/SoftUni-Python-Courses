input_num_as_string = input()
first_num = int(input_num_as_string[2])
second_num = int(input_num_as_string[1])
third_num = int(input_num_as_string[0])

for i in range(1, first_num + 1):
    for j in range(1, second_num + 1):
        for k in range(1, third_num + 1):
            print(f"{i} * {j} * {k} = {i * j * k};")

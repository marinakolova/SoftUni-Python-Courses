import operator

odd_even_mutator = lambda x: f'{x} - even' if x % 2 == 0 else f'{x} - odd'
operations = {
    "+": {'operation': operator.add, 'result_mutator': odd_even_mutator},
    "-": {'operation': operator.sub, 'result_mutator': odd_even_mutator},
    "*": {'operation': operator.mul, 'result_mutator': odd_even_mutator},
    "/": {'operation': operator.truediv, 'result_mutator': lambda x: f'{x:.2f}'},
    "%": {'operation': operator.mod, 'result_mutator': lambda x: x}
}

first_number = int(input())
second_number = int(input())
operation = input()

if (operation == "/" or operation == "%") and second_number == 0:
    print(f"Cannot divide {first_number} by zero")
    exit()

initial_result = operations[operation]['operation'](first_number, second_number)
final_result = operations[operation]['result_mutator'](initial_result)
print(f'{first_number} {operation} {second_number} = {final_result}')

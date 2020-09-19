import operator

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod
}

first_number = int(input())
second_number = int(input())
operation = input()

if (operation == "/" or operation == "%") and second_number == 0:
    print(f"Cannot divide {first_number} by zero")
    exit()

result = operations[operation](first_number, second_number)

if operation == "+" or operation == "-" or operation == "*":
    if result % 2 == 0:
        print(f"{first_number} {operation} {second_number} = {result} - even")
    else:
        print(f"{first_number} {operation} {second_number} = {result} - odd")

elif operation == "/":
    print(f"{first_number} {operation} {second_number} = {result:.2f}")

elif operation == "%":
    print(f"{first_number} {operation} {second_number} = {result}")

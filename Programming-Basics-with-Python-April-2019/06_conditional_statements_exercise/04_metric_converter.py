num = float(input())
input_unit = input()
output_unit = input()

result = 0

if input_unit == "m":

    if output_unit == "cm":
        result = num * 100
    elif output_unit == "mm":
        result = num * 1000

elif input_unit == "cm":

    if output_unit == "m":
        result = num / 100
    elif output_unit == "mm":
        result = num * 10

elif input_unit == "mm":

    if output_unit == "m":
        result = num / 1000
    elif output_unit == "cm":
        result = num / 10

print(f"{result:.3f}")

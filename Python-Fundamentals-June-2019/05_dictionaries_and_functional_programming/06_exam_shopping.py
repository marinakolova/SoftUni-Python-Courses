quantities = dict()

while True:
    inp = input()
    if inp == 'shopping time':
        break

    inp = inp.split(' ')
    if len(inp) != 3:
        continue

    command, product_name, quantity = inp
    if command != 'stock':
        continue

    quantities[product_name] = quantities.get(product_name, 0) + int(quantity)

while True:
    inp = input()
    if inp == 'exam time':
        break

    inp = inp.split(' ')

    if len(inp) != 3:
        continue

    command, product_name, quantity = inp
    if command != 'buy':
        continue

    if product_name not in quantities:
        print(f"{product_name} doesn't exist")
        continue

    if quantities[product_name] == 0:
        print(f"{product_name} out of stock")
        continue

    new_quantity = quantities[product_name] - int(quantity)
    if new_quantity <= 0:
        quantities[product_name] = 0
    else:
        quantities[product_name] = new_quantity

for product_name, quantity in quantities.items():
    if quantity:
        print(f"{product_name} -> {quantity}")

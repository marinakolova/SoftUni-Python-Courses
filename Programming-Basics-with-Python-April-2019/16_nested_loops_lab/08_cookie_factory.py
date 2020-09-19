batches_needed = int(input())
successful_batches = 0
flour = False
eggs = False
sugar = False

while successful_batches < batches_needed:
    product = input()
    if product == "flour":
        flour = True
    elif product == "eggs":
        eggs = True
    elif product == "sugar":
        sugar = True
    elif product == "Bake!":
        if flour and eggs and sugar:
            successful_batches += 1
            print(f"Baking batch number {successful_batches}...")
            flour = False
            eggs = False
            sugar = False
        else:
            print("The batter should contain flour, eggs and sugar!")

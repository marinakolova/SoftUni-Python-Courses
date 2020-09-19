cake_width = int(input())
cake_length = int(input())
cake_pieces = cake_width * cake_length

while True:
    command = input()
    if command == "STOP":
        pieces_left = cake_pieces
        print(f"{pieces_left} pieces are left.")
        break
    taken_pieces = int(command)
    if cake_pieces >= taken_pieces:
        cake_pieces -= taken_pieces
    elif cake_pieces < taken_pieces:
        pieces_needed = taken_pieces - cake_pieces
        print(f"No more cake left! You need {pieces_needed} pieces more.")
        break

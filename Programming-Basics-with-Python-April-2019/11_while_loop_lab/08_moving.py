room_width = int(input())
room_length = int(input())
room_height = int(input())
room_space = room_height * room_length * room_width
space_taken = 0

while True:
    command = input()
    if command == 'Done':
        space_left = room_space - space_taken
        if space_left > 0:
            print(f'{space_left} Cubic meters left.')
        break

    space_taken += int(command)
    if space_taken > room_space:
        needed_space = space_taken - room_space
        print(f'No more free space! You need {needed_space} Cubic meters more.')
        break

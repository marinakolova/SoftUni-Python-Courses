goal = 10000
steps_walked = 0
reached = False
while True:
    command = input()
    if command == 'Going home':
        steps_walked += int(input())
        if steps_walked >= goal:
            print('Goal reached! Good job!')
            reached = True
        break
    elif command == '':
        if steps_walked >= goal:
            print('Goal reached! Good job!')
            reached = True
            break
    else:
        steps_walked += int(command)
        if steps_walked >= goal:
            print('Goal reached! Good job!')
            reached = True
            break

if not reached:
    print(f'{goal - steps_walked} more steps to reach goal.')

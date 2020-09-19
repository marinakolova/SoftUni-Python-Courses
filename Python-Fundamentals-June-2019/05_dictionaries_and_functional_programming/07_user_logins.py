usernames = dict()
unsuccessful_logins = 0

while True:
    inp = input()
    if inp == 'login':
        break
    username, password = inp.split(' -> ')
    usernames[username] = password

while True:
    inp = input()
    if inp == 'end':
        print(f'unsuccessful login attempts: {unsuccessful_logins}')
        break

    username, password = inp.split(' -> ')
    if username not in usernames or usernames[username] != password:
        print(f'{username}: login failed')
        unsuccessful_logins += 1
    else:
        print(f'{username}: logged in successfully')
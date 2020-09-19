from collections import defaultdict

posts = defaultdict(dict)

while True:
    inp = input()
    if inp == 'drop the media':
        break

    inp = inp.split(' ')
    command = inp[0]
    rest_input = inp[1:]

    if command == 'post':
        posts[rest_input[0]] = {'likes': 0, 'dislikes': 0, 'comments': []}
    elif command == 'like':
        posts[rest_input[0]]['likes'] += 1
    elif command == 'dislike':
        posts[rest_input[0]]['dislikes'] += 1
    elif command == 'comment':
        post_name, commentator, *content = rest_input
        posts[post_name]['comments'].append({'commentator': commentator, 'content': ' '.join(content)})

for post_name, data in posts.items():
    print(f'Post: {post_name} | Likes: {data["likes"]} | Dislikes: {data["dislikes"]}')
    print('Comments:')
    if data['comments']:
        for comment in data['comments']:
            print(f'*  {comment["commentator"]}: {comment["content"]}')
    else:
        print('None')

class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


class User:
    def __init__(self, username):
        self.username = username
        self.messages = []


users = dict()

while True:
    info = input().split(" ")
    if len(info) == 1:
        break

    if len(info) == 2:
        username = info[1]
        users.__setitem__(username, User(username))

    if len(info) > 2:
        sender = info[0]
        receiver = info[2]
        content = info[3]

        if users.__contains__(sender) and users.__contains__(receiver):
            sms = Message(content,sender)
            users[receiver].messages.append(sms)

chat = input().split(" ")
messages_of_second = list(filter(lambda x: x.sender == chat[1],users[chat[0]].messages))
messages_of_first = list(filter(lambda x: x.sender == chat[0],users[chat[1]].messages))
conversation = list(zip(messages_of_first + [None] * (len(messages_of_second) - len(messages_of_first)),
                        messages_of_second + [None] * (len(messages_of_first) - len(messages_of_second))))

if conversation.__len__() == 0:
    print("No messages")
    exit()

for ch in conversation:
    if ch[0]:
        print(f"{ch[0].sender}: {ch[0].content}")

    if ch[1]:
        print(f"{ch[1].content} :{ch[1].sender}")

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.chapters = []


stock = {}
sold = []
money = 0

while True:
    inp = input()
    if inp == "on work":
        break

    inp_halves = inp.split(" -> ")
    info = inp_halves[0].split(" ")
    title = info[0]
    if len(info) < 3:
        continue
    author = info[1]
    try:
        price = float(info[2])
    except:
        continue

    if not title or not author or price <= 0:
        continue
    chapters = inp_halves[1].split(", ")
    book_to_add = Book(title, author, price)
    book_to_add.chapters = chapters
    stock[title] = book_to_add

while True:
    searched_title = input()
    if searched_title == "end work":
        break

    if searched_title not in stock:
        print("No such book here")

    if searched_title in stock:
        sold.append(stock[searched_title])
        money += stock[searched_title].price

if sold:
    for book in sold:
        print(f"SOLD: {book.title} with author {book.author}. "
              f"Chapters in the book {len(book.chapters)}")
    print(f"Money: {money:.2f}")
else:
    print("Bad day :(")

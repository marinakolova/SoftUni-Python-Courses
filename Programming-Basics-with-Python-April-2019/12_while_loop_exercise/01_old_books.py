book = input()
capacity = int(input())

books_count = 0
found_the_book = False

while True:
    inp = input()
    if inp == book:
        found_the_book = True
        break
    books_count += 1
    if books_count == capacity:
        break

if found_the_book:
    print(f"You checked {books_count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {books_count} books.")

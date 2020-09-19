class Book:

    MIN_TITLE_LENGTH = 3

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if len(title) < self.MIN_TITLE_LENGTH:
            raise ValueError('Title not valid!')
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if ' ' in author:
            first_name, second_name = author.split(' ')
            if second_name[0].isdigit():
                raise ValueError('Author not valid!')
        self._author = author

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError('Price not valid!')
        self._price = price

    def __str__(self):
        book = f'Type: {self.__class__.__name__}\n' \
            f'Title: {self.title}\n' \
            f'Author: {self.author}\n' \
            f'Price: {self.price:.2f}\n'
        return book


class GoldenEditionBook(Book):

    def __init__(self, title, author, price):
        super().__init__(title, author, price)

    def __str__(self):
        book = f'Type: {self.__class__.__name__}\n' \
            f'Title: {self.title}\n' \
            f'Author: {self.author}\n' \
            f'Price: {self.price * 1.3:.2f}\n'
        return book


if __name__ == '__main__':
    try:
        author = input()
        title = input()
        price = float(input())
        book = Book(title, author, price)
        golden_book = GoldenEditionBook(title, author, price)
        print(book)
        print(golden_book)
    except ValueError as e:
        print(e)

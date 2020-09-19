class Person:

    MIN_NAME_LENGTH = 3

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) < self.MIN_NAME_LENGTH:
            raise ValueError("Name's length should not be less than 3 symbols!")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def __str__(self):
        return f'Name: {self._name}, Age: {self._age}'


class Child(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError('Age must be positive!')
        if age > 15:
            raise ValueError("Child's age must be less than 15!")
        self._age = age


if __name__ == '__main__':
    name = input()
    age = int(input())
    try:
        child = Child(name, age)
        print(child)
    except ValueError as e:
        print(e)

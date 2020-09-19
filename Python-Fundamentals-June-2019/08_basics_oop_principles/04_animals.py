from abc import abstractmethod


class Animal:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Invalid input!')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        value = int(value)
        if not value or value < 0:
            raise ValueError('Invalid input!')
        self._age = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if not value:
            raise ValueError('Invalid input!')
        self._gender = value

    def __str__(self):
        return f'{self.name} {self.age} {self.gender}'

    @abstractmethod
    def produce_sound(self):
        pass


class Dog(Animal):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        print('Woof!')


class Frog(Animal):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        print('Ribbit')


class Cat(Animal):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def produce_sound(self):
        print('Meow meow')


class Kitten(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, 'Female')

    def produce_sound(self):
        print('Meow')


class Tomcat(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, 'Male')

    def produce_sound(self):
        print('MEOW')


def get_animal_instance(animal, name, age, gender):
    if animal == 'Dog':
        return Dog(name, age, gender)
    elif animal == 'Cat':
        return Cat(name, age, gender)
    elif animal == 'Frog':
        return Frog(name, age, gender)
    elif animal == 'Kitten':
        return Kitten(name, age)
    elif animal == 'Tomcat':
        return Tomcat(name, age)
    else:
        raise ValueError('Invalid input!')


if __name__ == '__main__':
    animals = []
    while True:
        inp = input()
        if inp == 'Beast!':
            for animal in animals:
                print(animal.__class__.__name__)
                print(animal)
                animal.produce_sound()
            break

        animal_type = inp
        name, age, gender = input().split(' ')
        try:
            animals.append(get_animal_instance(animal_type, name, age, gender))
        except ValueError as e:
            print(e)

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):

    def __init__(self, name, age, number_of_legs):
        super().__init__(name, age)
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")

    def __str__(self):
        return f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}'


class Cat(Animal):

    def __init__(self, name, age, intelligence_quotient):
        super().__init__(name, age)
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")

    def __str__(self):
        return f'Cat: {self.name}, Age: {self.age}, IQ: {self.intelligence_quotient}'


class Snake(Animal):

    def __init__(self, name, age, cruelty_coefficient):
        super().__init__(name, age)
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

    def __str__(self):
        return f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty_coefficient}'


if __name__ == '__main__':
    dogs, cats, snakes = [], [], []
    while True:
        inp = input()
        if inp == "I'm your Huckleberry":
            for animals in [dogs, cats, snakes]:
                for animal in animals:
                    print(animal)
            break

        inp = inp.split(' ')
        if len(inp) == 2 and inp[0] == 'talk':
            name = inp[1]
            found = False
            for animals in [dogs, cats, snakes]:
                if found:
                    break
                for animal in animals:
                    if animal.name == name:
                        animal.produce_sound()
                        found = True
                        break
        else:
            cls = inp[0]
            name = inp[1]
            age = int(inp[2])
            parameter = int(inp[3])
            if cls == 'Dog':
                dogs.append(Dog(name, age, parameter))
            elif cls == 'Cat':
                cats.append(Cat(name, age, parameter))
            else:
                snakes.append(Snake(name, age, parameter))

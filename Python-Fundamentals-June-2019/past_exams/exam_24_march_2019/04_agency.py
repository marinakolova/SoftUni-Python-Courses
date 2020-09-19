from abc import ABC, abstractmethod


class Apartment(ABC):
    def __init__(self, id, rooms, baths, square_meters, price):
        self.id = id
        self.rooms = int(rooms)
        self.baths = int(baths)
        self.square_meters = float(square_meters)
        self.price = float(price)
        self.is_taken = False

    @abstractmethod
    def __str__(self):
        return f"{self.rooms} rooms place with {self.baths} bathroom/s.\n{self.square_meters} sq. meters for {self.price} lv."


class LivingApartment(Apartment):
    def __init__(self, id, rooms, baths, square_meters, price):
        Apartment.__init__(self, id, rooms, baths, square_meters, price)

    def __str__(self):
        return Apartment.__str__(self)


class OfficeApartment(Apartment):
    def __init__(self, id, rooms, baths, square_meters, price):
        Apartment.__init__(self, id, rooms, baths, square_meters, price)

    def __str__(self):
        return Apartment.__str__(self)


data = input()
apartments_list = []

while not data == "start_selling":
    try:
        current_app = eval(data)
        apartments_list.append(current_app)
    except Exception as ex:
        print(ex)

    data = input()

data_list = input().split()
ids_list = list(map(lambda a: a.id, apartments_list))

while not (data_list[0] == "free" or data_list[0] == "taken"):
    command = data_list[0]
    id = data_list[1]

    if id in ids_list:
        current_app: Apartment = list(filter(lambda a: a.id == id, apartments_list))[0]
        if current_app.is_taken:
            print(f"Apartment with id - {id} is already taken!")
        elif command == "rent" and isinstance(current_app, LivingApartment):
            print(f"Apartment with id - {id} is only for selling!")
        elif command == "buy" and isinstance(current_app, OfficeApartment):
            print(f"Apartment with id - {id} is only for renting!")
        else:
            current_app.is_taken = True
    else:
        print(f"Apartment with id - {id} does not exist!")

    data_list = input().split()

if data_list[0] == 'taken':
    taken_ap_list = list(filter(lambda a: a.is_taken == True, apartments_list))
    for apartment in sorted(taken_ap_list, key=lambda a: (a.price, -a.square_meters)):
        print(apartment)

elif data_list[0] == 'free':
    taken_ap_list = list(filter(lambda a: a.is_taken == False, apartments_list))
    for apartment in sorted(taken_ap_list, key=lambda a: (-a.price, a.square_meters)):
        print(apartment)

if len(taken_ap_list) == 0:
    print("No information for this query")

class Biologist:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.researched_species = []

    def add_species(self, value_to_add):
        if type(value_to_add) is not Species:
            raise Exception("This is not a species")
        else:
            self.researched_species.append(value_to_add)

    def __str__(self):
        info = f"{self.name} is {self.age} years old Biologist with " \
               f"{len(self.researched_species)} researched species:"
        if self.researched_species:
            speciess = ""
            for spec in sorted(self.researched_species, key=lambda species: species.name):
                speciess += "\n" + str(spec)
            return info + speciess
        else:
            return info


class Chemist:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.researched_elements = []

    def add_element(self, value_to_add):
        if type(value_to_add) is not Element:
            raise Exception("This is not an element")
        else:
            self.researched_elements.append(value_to_add)

    def __str__(self):
        info = f"{self.name} is {self.age} years old Chemist with " \
               f"{len(self.researched_elements)} researched elements:"
        if self.researched_elements:
            elements = ""
            for el in sorted(self.researched_elements, key=lambda element: element.name):
                elements += "\n" + str(el)
            return info + elements
        else:
            return info


class Species:
    def __init__(self, name, typee):
        self.name = name
        self.typee = typee

    def __str__(self):
        return f"- {self.name} ({self.typee})"


class Element:
    def __init__(self, name, typee):
        self.name = name
        self.typee = typee

    def __str__(self):
        return f"- {self.name} ({self.typee})"


biologists = {}
chemists = {}
species_and_elements = {}

n = int(input())

for i in range(n):
    new_object = eval(input())
    name = new_object.name
    if type(new_object) is Biologist:
        biologists[name] = new_object
    elif type(new_object) is Chemist:
        chemists[name] = new_object
    elif type(new_object) is Element or type(new_object) is Species:
        species_and_elements[name] = new_object

m = int(input())

for i in range(m):
    command_tokens = input().split("-")
    scientist_name = command_tokens[0]
    command = command_tokens[1]
    species_or_element_name = command_tokens[2]

    if scientist_name not in biologists and scientist_name not in chemists:
        print("No such scientist")
        continue

    elif species_or_element_name not in species_and_elements:
        print("No such element or species")
        continue

    elif command == "add_species":
        if scientist_name not in biologists:
            print("Scientist has no such method")
        else:
            try:
                biologists[scientist_name].add_species(species_and_elements[species_or_element_name])
            except Exception as ex:
                print(ex)
                continue

    elif command == "add_element":
        if scientist_name not in chemists:
            print("Scientist has no such method")
        else:
            try:
                chemists[scientist_name].add_element(species_and_elements[species_or_element_name])
            except Exception as ex:
                print(ex)
                continue

    elif command.__contains__("str"):
        if scientist_name in biologists:
            print(biologists[scientist_name])
        elif scientist_name in chemists:
            print(chemists[scientist_name])

    else:
        print("Scientist has no such method")

all_scientists = list(biologists.values()) + list(chemists.values())

for sci in sorted(all_scientists, key=lambda scientist: (-scientist.age, scientist.name)):
    print(sci)

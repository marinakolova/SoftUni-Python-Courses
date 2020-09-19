class Country:
    def __init__(self, name):
        self.name = name
        self.percent_infections = 0
        self.quarantine = False


countries_by_name = {}
countries_input = input().split(", ")
for country_name in countries_input:
    country_to_add = Country(country_name)
    countries_by_name[country_name] = country_to_add

days = int(input())

for i in range(days):
    command = input().split()
    affected_country = command[1]

    if command[0] == "Fast_Infect":
        if countries_by_name[affected_country].quarantine:
            print(f"{affected_country} is under quarantine")
        else:
            countries_by_name[affected_country].percent_infections += 20

    elif command[0] == "Slow_Infect":
        if countries_by_name[affected_country].quarantine:
            print(f"{affected_country} is under quarantine")
        else:
            countries_by_name[affected_country].percent_infections += 10

    elif command[0] == "Quarantine":
        if countries_by_name[affected_country].quarantine:
            print(f"{affected_country} is already under quarantine")
        else:
            countries_by_name[affected_country].quarantine = True

    elif command[0] == "Cure":
        countries_by_name[affected_country].percent_infections = 0

countries_to_print = list(countries_by_name.values())

for countr in sorted(countries_to_print, key=lambda country: country.percent_infections, reverse=True):
    print(f"{countr.name} - {countr.percent_infections}% infected")

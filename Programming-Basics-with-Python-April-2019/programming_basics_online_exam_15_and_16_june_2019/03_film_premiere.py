john_wick = {"Drink": 12, "Popcorn": 15, "Menu": 19}
star_wars = {"Drink": 18, "Popcorn": 25, "Menu": 30}
jumanji = {"Drink": 9, "Popcorn": 11, "Menu": 14}

movie = input()
package = input()
count = int(input())
total_bill = 0

if movie == "John Wick":
    total_bill = john_wick[package] * count
elif movie == "Star Wars":
    total_bill = star_wars[package] * count
    if count >= 4:
        total_bill -= 0.3 * total_bill
elif movie == "Jumanji":
    total_bill = jumanji[package] * count
    if count == 2:
        total_bill -= 0.15 * total_bill

print(f"Your bill is {total_bill:.2f} leva.")

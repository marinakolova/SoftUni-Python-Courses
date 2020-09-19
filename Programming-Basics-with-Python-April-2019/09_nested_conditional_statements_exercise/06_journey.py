budget = float(input())
season = input()

destination = ""
price = 0
accommodation = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = 0.30 * budget
        accommodation = "Camp"
    elif season == "winter":
        price = 0.70 * budget
        accommodation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = 0.40 * budget
        accommodation = "Camp"
    elif season == "winter":
        price = 0.80 * budget
        accommodation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    price = 0.90 * budget
    accommodation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodation} - {price:.2f}")

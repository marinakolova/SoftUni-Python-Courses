kilometers = int(input())
part_of_the_day = input()

taxi_price = float("infinity")
bus_price = float("infinity")
train_price = float("infinity")

if kilometers >= 100:
    train_price = kilometers * 0.06

if kilometers >= 20:
    bus_price = kilometers * 0.09

if part_of_the_day == "day":
    taxi_price = 0.70 + kilometers * 0.79
else:
    taxi_price = 0.70 + kilometers * 0.90

print(f"{min(taxi_price, bus_price, train_price):.2f}")

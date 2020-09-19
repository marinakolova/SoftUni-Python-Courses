passengers = int(input())
stops = int(input())

for i in range(0, stops):
    passengers -= int(input())
    passengers += int(input())

if stops % 2 != 0:
    passengers += 2

print(f"The final number of passengers is : {passengers}")

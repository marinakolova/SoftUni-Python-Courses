hours = int(input())
mins = int(input())

mins += 15

if mins >= 60:
    hours += 1
    mins -= 60

if hours == 24:
    hours = 0

if mins < 10:
    print(f"{hours}:0{mins}")
else:
    print(f"{hours}:{mins}")

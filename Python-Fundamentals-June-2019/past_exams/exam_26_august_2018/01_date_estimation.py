import datetime

today = datetime.date(2018, 8, 26)

inp_tokens = input().split("-")

input_date = datetime.date(int(inp_tokens[0]), int(inp_tokens[1]), int(inp_tokens[2]))

if input_date < today:
    print("Passed")
elif input_date == today:
    print("Today date")
else:
    days_left = input_date - today + datetime.timedelta(days=1)
    print(f"{days_left.days} days left")

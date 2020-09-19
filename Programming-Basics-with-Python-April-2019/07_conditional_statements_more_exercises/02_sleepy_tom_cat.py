holidays = int(input())
working_days = 365 - holidays
playtime = holidays * 127 + working_days * 63
normal_playtime = 30000

if playtime > normal_playtime:
    print("Tom will run away")
    time_left_in_mins = playtime - normal_playtime
    hours_left = int(time_left_in_mins / 60)
    mins_left = time_left_in_mins % 60
    print(f"{hours_left} hours and {mins_left} minutes more for play")
else:
    print("Tom sleeps well")
    time_more_int_mins = normal_playtime - playtime
    hours_more = int(time_more_int_mins / 60)
    mins_more = time_more_int_mins % 60
    print(f"{hours_more} hours and {mins_more} minutes less for play")

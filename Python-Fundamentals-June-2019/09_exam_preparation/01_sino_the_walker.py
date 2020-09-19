import datetime

leaving_time_input = input().split(":")
leaving_hour = int(leaving_time_input[0])
leaving_mins = int(leaving_time_input[1])
leaving_secs = int(leaving_time_input[2])

leaving_time = datetime.datetime(1, 1, 1, leaving_hour, leaving_mins, leaving_secs)

steps = int(input())
secs_per_step = int(input())

walking_time_in_secs = (steps * secs_per_step)

arrival_time = leaving_time + datetime.timedelta(seconds=walking_time_in_secs)

print(f"Time Arrival: {arrival_time.hour:02d}:{arrival_time.minute:02d}:{arrival_time.second:02d}")

import math

record = float(input())
meters = float(input())
time_for_1_meter = float(input())

total_time = meters * time_for_1_meter
meters_for_delay = meters / 15
meters_for_delay_rounded = math.trunc(meters_for_delay)
delay = meters_for_delay_rounded * 12.5

total_time_with_delay = total_time + delay

time_needed = total_time_with_delay - record

if time_needed < 0:
    print(f"Yes, he succeeded! The new world record is {total_time_with_delay:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")

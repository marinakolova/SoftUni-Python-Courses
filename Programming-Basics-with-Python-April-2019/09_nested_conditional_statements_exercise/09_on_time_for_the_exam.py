exam_hour = int(input())
exam_mins = int(input())
arrival_hour = int(input())
arrival_mins = int(input())

total_exam_mins = exam_hour * 60 + exam_mins
total_arrival_mins = arrival_hour * 60 + arrival_mins

time_diff_in_mins = abs(total_arrival_mins - total_exam_mins)
result = ""
total_result = ""

if total_exam_mins < total_arrival_mins:
    result = "Late"
    if time_diff_in_mins <= 59:
        total_result = f"{time_diff_in_mins} minutes after the start"
    else:
        hours = int(time_diff_in_mins / 60)
        mins = time_diff_in_mins % 60
        total_result = f"{hours:.0f}:{mins:02d} hours after the start"

elif total_exam_mins >= total_arrival_mins:
    if time_diff_in_mins > 30:
        result = "Early"
        if time_diff_in_mins <= 59:
            total_result = f"{time_diff_in_mins} minutes before the start"
        else:
            hours = int(time_diff_in_mins / 60)
            mins = time_diff_in_mins % 60
            total_result = f"{hours:.0f}:{mins:02d} hours before the start"
    else:
        result = "On time"
        total_result = f"{time_diff_in_mins} minutes before the start"

print(result)
print(total_result)

actor = input()
total_points = float(input())
needed_points = 1250.5
n = int(input())

for i in range(0, n):
    judge_name = input()
    judge_points = float(input())
    points = ((len(judge_name) * judge_points) / 2)
    total_points += points
    if total_points >= needed_points:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
        exit()

print(f"Sorry, {actor} you need {(needed_points - total_points):.1f} more!")

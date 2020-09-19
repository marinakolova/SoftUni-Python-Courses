shooting_time = int(input())
acts_count = int(input())
act_duration = int(input())

used_time = shooting_time * 0.15 + acts_count * act_duration

if shooting_time >= used_time:
    print(f"You managed to finish the movie on time! "
          f"You have {round(shooting_time - used_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need "
          f"{round(used_time - shooting_time)} minutes.")

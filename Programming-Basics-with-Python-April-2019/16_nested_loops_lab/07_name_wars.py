name = input()

max_sum = 0
winner = None

while name != "STOP":
    sum_name = 0
    for letter in name:
        sum_name += ord(letter)
    if max_sum < sum_name:
        max_sum = sum_name
        winner = name
    name = input()

print(f"Winner is {winner} - {max_sum}!")

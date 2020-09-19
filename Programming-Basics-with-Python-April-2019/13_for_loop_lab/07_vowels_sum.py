input_string = input()
sum = 0

vowels_values = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5
}

for char in input_string:
    if char in vowels_values:
        sum += vowels_values[char]

print(sum)

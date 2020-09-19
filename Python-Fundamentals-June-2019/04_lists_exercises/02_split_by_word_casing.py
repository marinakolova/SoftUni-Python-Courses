user_input = input()

delimiters = (',', ';', ':',  '.', '!',  '(',  ')',  '"', "'", '\\', '/', '[', ']')

for delimiter in delimiters:
    user_input = user_input.replace(delimiter, ' ')

words = [word for word in user_input.split(' ') if word]
lower_case_words, upper_case_words, mixed_case_words = [], [], []

for word in words:
    if word.isalpha():
        if word.lower() == word:
            lower_case_words.append(word)
        elif word.upper() == word:
            upper_case_words.append(word)
        else:
            mixed_case_words.append(word)
    else:
        mixed_case_words.append(word)

print('Lower-case: ' + ', '.join(lower_case_words))
print('Mixed-case: ' + ', '.join(mixed_case_words))
print('Upper-case: ' + ', '.join(upper_case_words))

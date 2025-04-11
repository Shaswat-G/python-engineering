# Find the most reppeating charachter in a string
from pprint import pp
sentence = "This is a common interview question"

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency = sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)
pp(char_frequency)
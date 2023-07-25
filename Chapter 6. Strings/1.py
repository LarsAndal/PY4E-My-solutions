"""
Write a while loop that starts at the last character in the
string and works its way backwards to the first character in
the string, printing each letter on a separate line,
except backwards.

"""

word = input("Enter a word: ")
length = len(word)

i = 0
index = -1
while i < length:
    print(word[index])
    i = i + 1
    index = index - 1

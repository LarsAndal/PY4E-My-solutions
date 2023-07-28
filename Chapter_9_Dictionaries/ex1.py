"""Exercise 1.

Write a program that reads the words in words.txt and stores
them as keys in a dictionary. It doesn't matter what the
values are. Then you can use the in operator as a fast way
to check whether a string is in the dictionary.
"""

file_handler = open("words.txt", encoding="utf-8")  # pylint: disable=R1732
words = {}
for line in file_handler:
    line = line.split()
    for word in line:
        words[word] = ""
print(words)

if "kinds" in words:
    print(True)
else:
    print(False)

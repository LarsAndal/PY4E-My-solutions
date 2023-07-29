"""Exercise 3.

Write a program that reads a ﬁle and prints the letters in
decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program
should not count spaces, digits, punctuation, or anything other
than the letters a-z. Find text samples from several different
languages and see how letter frequency varies between languages.
Compare your results with the tables at
https://wikipedia.org/wiki/Letter_frequencies.
"""

import string

try:
    filename = input("Enter a file name: ")
    file_handler = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print("Invalid file name")
    exit()  # pylint: disable=R1722

letters_dict = {}
for line in file_handler:
    line = line.strip()
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.translate(line.maketrans("", "", string.digits))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter not in letters_dict:
                letters_dict[letter] = 1
            else:
                letters_dict[letter] += 1

# print(f"\nDebug {letters_dict}\n")
letters_list = []
for key, val in letters_dict.items():
    letters_list.append((val, key))

# print(f"\nDebug {letters_list}\n")
letters_list.sort(reverse=True)
# print(f"\nDebug {letters_list}\n")

for key, val in letters_list:
    print(key, val)

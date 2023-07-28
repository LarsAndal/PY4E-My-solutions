"""Exercise 3.

Rewrite the guardian code in the above example without
two if statements. Instead, use a compound logical
expression using the or logical operator with a single
if statement.

Example:
fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    words = line.split()
    # print("Debug: ", words)
    if len(words) <= 1:
        continue
    if words[0] != "From":
        continue
    print(words[2])
"""

# pylint: disable=R1732
file_handler = open("../Chapter_7_Files/mbox-short.txt", encoding="utf-8")
# pylint: enable=R1732
for line in file_handler:
    words = line.split()
    if len(words) <= 2 or words[0] != "From":
        continue
    print(words[2])

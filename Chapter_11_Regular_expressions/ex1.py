"""Exercise 1.

Write a simple program to simulate the operation of the grep
command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$
"""

import re

FILENAME = "../Chapter_7_Files/mbox.txt"
file_handler = open(FILENAME, encoding="utf-8")  # pylint:disable=R1732

regular_expression = input("Enter a regular expression: ")
count = 0  # pylint: disable=C0103
for line in file_handler:
    line.strip()
    regular = re.findall(regular_expression, line)
    if len(regular) > 0:
        count += 1

print(f"{FILENAME} had {count} lines that matched {regular_expression}")

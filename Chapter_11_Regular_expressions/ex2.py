"""Exercise 2.

Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
"""

import re

filename = input("Enter file: ")

try:
    file_handler = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print("Invalid filename")
    exit()  # pylint: disable=R1722

count = 0  # pylint: disable=C0103
total = 0  # pylint: disable=C0103
for line in file_handler:
    revision_list = re.findall("^New Revision: ([0-9.]*)", line)
    for revision in revision_list:
        count += 1
        total += int(revision)
        # print(f"\nDebug: {revision}\n")
print(f"{int(total/count)}")

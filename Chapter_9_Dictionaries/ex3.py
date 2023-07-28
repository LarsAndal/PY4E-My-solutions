"""Exercise 3.

Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from
each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""

filename = input("Enter a file name: ")
try:
    lines = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print("Invalid file name")
    exit()  # pylint: disable=R1722

weekday_histogram = {}
for line in lines:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        mail_address = line[1]
        weekday_histogram[mail_address] = (
            weekday_histogram.get(mail_address, 0) + 1
        )
print(weekday_histogram)

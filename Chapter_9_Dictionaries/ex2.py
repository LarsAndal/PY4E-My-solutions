"""Exercise 2.

Write a program that categorizes each mail message by which day
of the week the commit was done. To do this look for lines that
start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program
print out the contents of your dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""

filename: str = input("Enter a file name: ")
try:
    lines = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print("Invalid file name")
    exit()  # pylint: disable=R1722

date_histogram = {}
for line in lines:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        word = line[2]
        date_histogram[word] = date_histogram.get(word, 0) + 1
print(date_histogram)

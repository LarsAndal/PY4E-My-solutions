"""Exercise 4.

Add code to the above program to figure out who has the most
messages in the file. After all the data has been read and the
dictionary has been created, look through the dictionary using a
maximum loop (see Chapter 5: Maximum and minimum loops) to find who
has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

filename = input("Enter a file name: ")
try:
    lines = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print("Invalid file name")
    exit()  # pylint: disable=R1722

mail_histogram = {}
for line in lines:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        mail_address = line[1]
        mail_histogram[mail_address] = mail_histogram.get(mail_address, 0) + 1

mail_keys = list(mail_histogram.keys())
largest = None  # pylint: disable=C0103
for key in mail_keys:
    if largest is None or mail_histogram[key] > largest:
        largest = mail_histogram[key]
        mail = key
print(f"{mail} {largest}")

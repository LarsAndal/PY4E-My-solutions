"""Exercise 1.

Revise a previous program as follows: Read and parse the “From”
lines and pull out the addresses from the line. Count the number
of messages from each person using a dictionary.

After all the data has been read, print the person with the most
commits by creating a list of (count, email) tuples from the
dictionary. Then sort the list in reverse order and print out
the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

try:
    filename = input("Enter a file name: ")
    file_handler = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print("Invalid file name")
    exit()  # pylint: disable=R1722

mail_addresses_histogram = {}
for line in file_handler:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        mail_address = words[1]
        if mail_address not in mail_addresses_histogram:
            mail_addresses_histogram[mail_address] = 1
        else:
            mail_addresses_histogram[mail_address] += 1

# print(f"\nDebug: {mail_addresses_histogram}\n")

mail_addresses_list = []
for key, val in list(mail_addresses_histogram.items()):
    mail_addresses_list.append((val, key))

# print(f"\nDebug: {mail_addresses_list}\n")
mail_addresses_list.sort(reverse=True)
# print(f"\nDebug: {mail_addresses_list}\n")

for key, val in mail_addresses_list[:1]:
    print(val, key)

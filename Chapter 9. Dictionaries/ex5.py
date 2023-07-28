"""Exercise 5.

This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program,
print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""

filename = input("Enter a file name: ")
try:
    lines = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print("Invalid file name")
    exit()  # pylint: disable=R1722

domain_histogram = {}
for line in lines:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        mail_address = line[1]
        start = mail_address.find("@") + 1
        domain = mail_address[start:]
        domain_histogram[domain] = domain_histogram.get(domain, 0) + 1
print(domain_histogram)

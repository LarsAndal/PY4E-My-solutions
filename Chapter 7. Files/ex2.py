"""Exercise 2.

Write a program to prompt for a file name, and then read
through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the
line. Count these lines and then compute the total of the spam
confidence values from these lines. When you reach the end of
the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

Test your file on the mbox.txt and mbox-short.txt files.
"""

try:
    filename = input("Enter the file name: ")
    lines = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print("Invalid file name")

# pylint: disable=C0103
total = 0
counter = 0
SEARCH = "X-DSPAM-Confidence:"
for line in lines:
    if line.startswith(SEARCH):
        line = line.strip()
        start = line.find(" ")
        number = float(line[start:])
        total = total + number
        counter = counter + 1

average = total / counter
print(f"Average spam confidence: {average}")

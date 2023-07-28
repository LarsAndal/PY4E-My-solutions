"""Exercise 3.

Sometimes when programmers get bored or want to have a bit of
fun, they add a harmless Easter Egg to their program. Modify
the program that prompts the user for the file name so that
it prints a funny message when the user types in the exact
file name “na na boo boo”. The program should behave normally
for all other files which exist and don't exist. Here is a
sample execution of the program:

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!

We are not encouraging you to put Easter Eggs in your programs; this
is just an exercise.
"""

filename = input("Enter the file name: ")

if filename == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()  # pylint: disable=R1722

try:
    file = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print(f"File cannot be opened: {filename}")
    exit()  # pylint: disable=R1722

# pylint: disable=C0103
counter = 0
for line in file:
    line = line.lower()
    if line.find("subject") != -1:
        counter = counter + 1
        print(line)
print(f"There were {counter} subject lines in {filename}")

"""Exercise 1.

Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total,
count, and average of the numbers. If the user enters anything
other than a number, detect their mistake using try and except
and print an error message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333

Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and
minimum of the numbers instead of the average.
"""


def adder(lst):
    """Add all numbers together."""
    tot = 0
    for i in lst:
        tot = tot + i
    return tot


def number_reader():
    """Take numeric input from user and store it in a list.

    When the user enters 'done' the function calls the other functions.
    """
    numbers = []
    while True:
        line = input("Enter a number: ")
        if line == "done":
            count = len(numbers)
            total = adder(numbers)
            avg = total / count
            print(f"{total} {count} {avg}")
            break
        try:
            number = float(line)
            numbers.append(number)
        except ValueError:
            print("Invalid input")


number_reader()

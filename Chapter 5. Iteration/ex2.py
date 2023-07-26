"""Exercise 2.

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


def find_largest(lst):
    """Find the largest value in a list."""
    largest = None
    for i in lst:
        if largest is None or i > largest:
            largest = i
    return largest


def find_smallest(lst):
    """Find the smallest value in a list."""
    smallest = None
    for i in lst:
        if smallest is None or i < smallest:
            smallest = i
    return smallest


def number_reader():
    """Take numeric input from user and store it in a list.

    When the user enters 'done' the function calls the other functions.
    """
    numbers = []
    while True:
        line = input("Enter a number: ")
        if line == "done":
            maximum = find_largest(numbers)
            minimum = find_smallest(numbers)
            print(f"{maximum} {minimum}")
            break
        try:
            number = float(line)
            numbers.append(number)
        except ValueError:
            print("Invalid input")


number_reader()

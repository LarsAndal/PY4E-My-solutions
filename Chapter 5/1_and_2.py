"""
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
as above and at the end prints out both the maximum and minimum
of the numbers instead of the average.

"""

numbers = list()


def adder(x):
    t = 0
    for i in x:
        t = t + i
    return t


def findLargest(x):
    largest = None
    for i in x:
        if largest is None or i > largest:
            largest = i
    return largest


def findSmallest(x):
    smallest = None
    for i in x:
        if smallest is None or i < smallest:
            smallest = i
    return smallest


def numberReader():
    while True:
        line = input("Enter a number: ")
        if line == "done":
            count = len(numbers)
            total = adder(numbers)
            avg = total / count
            print(f"{total} {count} {avg}")
            maximum = findLargest(numbers)
            minimum = findSmallest(numbers)
            print(f"{maximum} {minimum}")
            break
        else:
            try:
                number = int(line)
                numbers.append(number)
            except:
                print("Invalid input")


numberReader()

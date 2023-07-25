"""
Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a
message and exiting the program. The following shows two
executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
"""

try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))
    threshold = 40
    overtime = 0
    if hours > threshold:
        overtime = hours - threshold
        hours = hours - overtime
    pay = hours * rate + overtime * rate * 1.5
    print(f"Pay: {pay}")
except:
    print("Error, please enter numeric input")

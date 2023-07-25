"""
Rewrite your pay computation with time-and-a-half for over-
time and create a function called computepay which takes two
parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""


def computepay(hours, rate):
    threshold = 40
    overtime = 0
    if hours > threshold:
        overtime = hours - threshold
        hours = hours - overtime
    pay = hours * rate + overtime * rate * 1.5
    return pay


try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay = computepay(hours, rate)
    print(f"Pay: {pay}")
except:
    print("Error, please enter numeric input")

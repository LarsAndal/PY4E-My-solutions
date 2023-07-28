"""Exercise 6.

Rewrite your pay computation with time-and-a-half for over-
time and create a function called "computepay" which takes two
parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""


def computepay(hour, rate):
    """Compute the gross pay.

    Args:
        hour (float): hours worked
        rate (float): money earned per hour

    Returns:
        float: pay
    """
    threshold = 40
    overtime = 0
    if hour > threshold:
        overtime = hour - threshold
        hour = hour - overtime
    gross_pay = hour * rate + overtime * rate * 1.5
    return gross_pay


try:
    input_hours = float(input("Enter Hours: "))
    input_rate = float(input("Enter Rate: "))
    pay = computepay(input_hours, input_rate)
    print(f"Pay: {pay}")
except TypeError:
    print("Error, please enter numeric input")

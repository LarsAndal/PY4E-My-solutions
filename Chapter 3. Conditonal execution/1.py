"""
Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

threshold = 40
overtime = 0
if hours > threshold:
    overtime = hours - threshold
    hours = hours - overtime
pay = hours * rate + overtime * rate * 1.5

print(f"Pay: {pay}")

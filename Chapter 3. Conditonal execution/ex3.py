"""Exercise 3.

Write a program to prompt for a score between
0.0 and 1.0. If the score is out of range,
print an error message. If the score is between
0.0 and 1.0, print a grade using the following table:

Score 	Grade
>= 0.9 	A
>= 0.8 	B
>= 0.7 	C
>= 0.6 	D
< 0.6 	F

Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F
"""

score = input("Enter score: ")
try:
    score = float(score)
    if 0 <= score <= 1:
        if score >= 0.9:
            GRADE = "A"
        elif score >= 0.8:
            GRADE = "B"
        elif score >= 0.7:
            GRADE = "C"
        elif score >= 0.6:
            GRADE = "D"
        else:
            GRADE = "F"
        print(GRADE)
    else:
        raise ValueError
except ValueError:
    print("Enter numeric input between 0 and 1.")
    print("Use '.' as decimal point.")

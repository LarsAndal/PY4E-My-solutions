"""
Encapsulate this code in a function named count, and
generalize it so that it accepts the string and the
letter as arguments.

"""

word = input("Enter a word: ").lower()
letter = input("Enter a letter: ").lower()


def count(word, letter):
    total = 0
    for i in word:
        if i == letter:
            total = total + 1
    print(total)


count(word, letter)

"""
There is a string method called count that is similar to
the function in the previous exercise. Read the documentation of this
method at:
https://docs.python.org/library/stdtypes.html#string-methods
Write an invocation that counts the number of times the letter a occurs
in “banana”.

"""
print("banana".count("a"))

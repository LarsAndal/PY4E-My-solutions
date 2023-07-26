"""Exercise 3.

Encapsulate this code in a function named count,
and generalize it so that it accepts the string
and the letter as arguments.
"""


def letter_counter(word, letter):
    """Count the number of letters in a word and output the total.

    Args:
        word (str): Entered by user
        letter (str): Entered by user
    """
    total = 0
    for i in word:
        if i == letter:
            total = total + 1
    print(total)


input_word = input("Enter a word: ").lower()
input_letter = input("Enter a letter: ").lower()
letter_counter(input_word, input_letter)

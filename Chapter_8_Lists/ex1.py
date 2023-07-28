"""Exercise 1.

Write a function called chop that takes a list and modifies it, removing the
first and last elements, and returns None. Then write a function called middle
that takes a list and returns a new list that contains all but the first and
last elements.
"""


def chop(lst):
    """Remove the first and last characters of a list and return None."""
    del lst[0]
    del lst[-1]


def middle(lst):
    """Return all but start and end of a list.

    Make a copy of the original list, removes the first and last
    characters of a list and returns the new list.
    """
    rest = lst.copy()
    del rest[0]
    del rest[-1]
    return rest


a_list = [1, 2, 3]
empty_list = chop(a_list)  # pylint: disable=E1111,C0103
print("Debug: ", a_list)
print("Debug: ", empty_list)

another_list = [4, 5, 6]
middle_list = middle(another_list)
print("Debug: ", another_list)
print("Debug: ", middle_list)

#!/usr/bin/python3
"""Define a print square function"""


def print_square(size):
    """Declare a function that prints a square with # character.

    Args:
        size: the length of the square.
    Raises:
        TypeError: If size is not integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for length in range(size):
        for width in range(size):
            print("#", end="")
        print()

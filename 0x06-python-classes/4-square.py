#!/usr/bin/python3
"""
"""
class Square:
    """Represents a square"""


    def __init__(self, value):
        """Initializes a new square object

        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """

#!/usr/bin/python3
"""
"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initialize a square

        Args:
            size: size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square

        Return: the area of the square
        """
        return self.__size ** 2

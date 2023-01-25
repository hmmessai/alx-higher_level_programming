#!/usr/bin/python3
"""
Defines a square class
"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a new square object

        Args:
            size: size of the square
        """
        self.__size = size

    def area(self):
        """Computes the area of the square

        Return: Area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value: the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

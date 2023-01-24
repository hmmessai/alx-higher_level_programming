#!/usr/bin/python3
"""
Defines a square class
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
        """Computes the area of the square

        Return: Area of the square
        """
        return self.__size ** 2
    
    def size(self):
        """Retrieve the size of the square"""

        return self.__size

    def size(self, value):
        """Sets the size of the square

        Args:
            value: the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


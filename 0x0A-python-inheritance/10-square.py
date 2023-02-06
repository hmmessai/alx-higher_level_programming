#!/usr/bin/python3
"""Defines the Square class."""


class Square(Rectangle):
    """Represents a square class."""

    def __init__(self, size):
        """Initializes the Square instance.

        Args:
            size: the size of the side of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Computes the area of the square."""
        return (self.__size ** 2)


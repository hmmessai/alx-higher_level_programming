#!/usr/bin/python3
"""Defines a square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square class that inherits from Rectangle class."""

    def __init__(self, size):
        """Initializes the square instance.

        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

#!/usr/bin/python3
"""Define Rectangle class."""


class Rectangle(BaseGeometry):
    """Represents a Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the Rectangle class instance.

        Args:
            width (int): the width of the rectangle.
            height (int): the heigt of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

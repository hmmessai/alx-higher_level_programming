#!/usr/bin/python3
"""Define Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the Rectangle class instance.

        Args:
            width (int): the width of the rectangle.
            height (int): the heigt of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of the rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """String representation of the object."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += self.__width + "/" + self.__height
        return string

#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a Rectangle."""

    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        Raises:
            TypeError: If width is not integer.
            ValueError: If width is less than 0.
            TypeError: If height is not integer.
            ValueError: If height is less than 0.
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieves a width variable."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets a width variable."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrives the height variable."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of an instance."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Printable representation of the Rectangle class."""
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append(type(self).print_symbol)
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Representation of the Rectangle class."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Defines the deletion operation."""
        if type(self).number_of_instances > 0:
            type(self).number_of_instances -= 1
        print("Bye rectangle...")



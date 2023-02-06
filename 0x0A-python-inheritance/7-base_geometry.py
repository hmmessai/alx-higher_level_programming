#!/usr/bin/python3
"""Defines the class BaseGeometry."""


class BaseGeometry:
    """Represents the class BaseGeometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value to be an integer.

        Args:
            name: the name of a value.
            value: the value of name.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

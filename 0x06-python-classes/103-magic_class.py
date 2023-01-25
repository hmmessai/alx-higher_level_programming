#!/usr/bin/python3
from math import pi
"""Define a MagicClass"""


class MagicClass:
    """Representation of MagicClass"""

    def __init__(self, radius=0):
        """Initialize the MagicClass object

        Arg:
            radius(int / float): the radius of the MagicClass object
        """
        if (not isinstance(radius, float) or not isinstance(radius, int)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Computes the area of the radius"""
        return (pi * self.__radius ** 2)

    def circumference(self):
        """Computes the circumference of the circle"""
        return (self.__radius * pi * 2)

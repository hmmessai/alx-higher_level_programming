#!/usr/bin/python3
"""Define a MagicClass"""

import math


class MagicClass:
    """Representation of circle"""

    def __init__(self, radius=0):
        """Initialize the circle object

        Arg:
            radius(int or float): the radius of the circle object
        """
        if (not isinstance(radius, float) or not isinstance(radius, int)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Computes the area of the circle"""
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        """Computes the circumference of the circle"""
        return (self.__radius * math.pi * 2)
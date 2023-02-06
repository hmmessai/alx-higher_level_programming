#!/usr/bin/python3
"""Defines MyList class."""


class MyList(list):
    """Represents a class MyList based on the built-in list class."""

    def print_sorted(self):
        """Prints a sorted form of list in ascending order."""
        print(sorted(self))

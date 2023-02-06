#!/usr/bin/python3
"""Defines the function is_same_class."""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of a_class.

    Args:
        obj: the object to check.
        a_class (type): The class to test the object with.
    Return:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

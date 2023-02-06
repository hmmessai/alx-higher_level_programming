#!/usr/bin/python3
"""Defines the function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is instance of a_class or any inherited class.

    Args:
        obj: the object to be checked.
        a_class: the class to be checked if obj is instance.
    Return:
        True - if obj is in fact instance of a_class.
        False - otherwise.
    """
    return isinstance(obj, a_class)

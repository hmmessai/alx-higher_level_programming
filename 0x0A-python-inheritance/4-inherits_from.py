#!/usr/bin/python3
"""Defines a function inherits_from."""


def inherits_from(obj, a_class):
    """Checks if the obj is an inherited instance of a_class.

    Args:
        obj: the object to be checked.
        a_class: the class to be checked.
    Return:
        True - if the obj is inherited from a_class.
        False - otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

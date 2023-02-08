#!/usr/bin/python3
"""Define a class to json function."""


def class_to_json(obj):
    """json serialization of an object with dictionary representation.

    Args:
        obj: an instance of a class.
    Return:
        dictionary representation of the object.
    """
    return obj.__dict__

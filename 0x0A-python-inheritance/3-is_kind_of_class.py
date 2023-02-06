#!/usr/bin/python3
"""Defines the function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is instance of a_class or any inherited class."""
    return isinstance(obj, a_class)

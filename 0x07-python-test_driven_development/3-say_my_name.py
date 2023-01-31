#!/usr/bin/python3
"""Defines a say my name function"""


def say_my_name(first_name, last_name=""):
    """Prints the name of a person

    Args:
        first_name(string): the first name of the person
        last_name(string): the last name of the person
    Raises:
        TypeError: If first and last name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")

    print("My name is {} {}".format(first_name, last_name))

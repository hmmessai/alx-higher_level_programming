#!/usr/bin/python3
"""Defines append write function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a utf-8 text file.

    Args:
        filename (str): the file to be updated.
        text (str): the text to be appended.
    Return:
        The number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Define the write file function."""


def write_file(filename="", text=""):
    """Writes a string to a utf-8 text file.

    Args:
        filename (str): the name of the text file.
        text (str): the text to be written into the text file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

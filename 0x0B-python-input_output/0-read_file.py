#!/usr/bin/python3
"""Defines a read file function."""


def read_file(filename=""):
    """Reads a UTF8 text file and prints it to stdout.

    Args:
        filename: the name of the file to read.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")

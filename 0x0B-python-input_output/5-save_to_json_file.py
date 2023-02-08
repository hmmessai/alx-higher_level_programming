#!/usr/bin/python3
"""Define save to json file function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using json.

    Args:
        my_obj: the object to be written.
        filename (str): the file to be written on.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

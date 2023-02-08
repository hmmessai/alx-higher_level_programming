#!/usr/bin/python3
"""Define from json string function."""
import json


def from_json_string(my_str):
    """Converts json string to a python structure.

    Args:
        my_str (str): the json string.
    Return:
        an object with python data structure.
    """
    return json.loads(my_str)

#!/usr/bin/python3
"""Defines to json string function."""
import json


def to_json_string(my_obj):
    """returns a json representation of an object.

    Args:
        my_obj (str): the object to be changed.
    Return:
        The json representation of my_obj.
    """
    return json.dumps(my_obj)

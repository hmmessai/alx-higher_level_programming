#!/usr/bin/python3
"""Defines load from json file function."""
import json


def load_from_json_file(filename):
    """Creates an object from a json file.

    Args:
        filename: the json file to be converted.
    """
    with open(filename) as f:
        return json.load(f)

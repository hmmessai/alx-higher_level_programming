#!/usr/bin/python3
"""Defines a class Student."""
import json


class Student:
    """Representation of a Student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a class instance.

        Args:
            first_name (str): the first name of student.
            last_name (str): the last name of student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student.

        Args:
            attrs: attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)

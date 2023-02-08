#!/usr/bin/python3
"""Defines a class Student."""


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

    def to_json(self):
        """Retrieves a dictionary representation of a Student."""
        return self.__dict__

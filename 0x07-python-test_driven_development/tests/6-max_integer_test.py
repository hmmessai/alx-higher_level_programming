#!/usr/bin/python3
"""Unittest for max_integer([...])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([...])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with one element."""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_float(self):
        """Test a list of floats."""
        floats = [1.54, 6.44, -9.78, 15.4, 6.0]
        self.assertEqual(max_integer(floats), 15.4)

    def test_ints_and_floats(self):
        """Test a list with ints and floats."""
        ints_and_floats = [1.53, 35.5, 6, -4, 0]
        self.assertEqual(max_integer(ints_and_floats), 35.5)

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == "__main__":
    unittest.main()

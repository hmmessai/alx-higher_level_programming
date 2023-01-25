#!/usr/bin/python3
"""
Define a square class
"""
class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initializes a square class
        Args:
            size(int): The size of the new square
        """
        self.size = size
    
    @property
    def size(self):
        """Retrieve the square class"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a value to the square class

        Args:
            value: value to set the class to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints # characters on stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

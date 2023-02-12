#!/usr/bin/python3
"""Defines a class Square that inherits from class Rectangle."""
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance of the class.

        Args:
            size (int): the size of the square.
            x (int): the x offset.
            y (int): the y offset.
            id (int): the id of the object.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Reterives size of the square."""
        return self.width

    @size.setter
    def size(self, size):
        """Sets a value to the size of square."""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the values of the square.

        Args:
            *args (ints): New attribute values.
                -1st argument represents id attribute.
                -2nd argument represents size attribute.
                -3rd argument represents x attribute.
                -4th argument represents y attribute.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary representation of a square."""
        return {
                "id" : self.id,
                "size" : self.size,
                "x" : self.x,
                "y" : self.y
                }

    def __str__(self):
        """String representation of the Square instance."""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                self.x, self.y,
                self.size)

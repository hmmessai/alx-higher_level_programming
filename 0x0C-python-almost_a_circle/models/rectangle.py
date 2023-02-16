#!/usr/bin/python3
"""Defines a Rectangle class."""
Base = __import__('base').Base


class Rectangle(Base):
    """Represents a Rectangle class object."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle class instance.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
            x (int): the x offset of the rectangle.
            y (int): the y offset of the rectangle.
            id: the id of the instance.
        Raises:
            TypeError: if all inputs are not integers.(excluding id)
            ValueError: if width or height is less than or equal to zero.
            ValueError: if x and y are less than zero.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Reterives the value of width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets a value to width."""
        if not isinstance(width , int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Reterives the value of height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets a value to height."""
        if not isinstance(height , int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Reterives the value of x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets a value to x."""
        if not isinstance(x , int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Reterives the value from y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets a value to y."""
        if not isinstance(y , int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Computes the area of the Rectangle."""
        return self.__height * self.__width

    def display(self):
        """Displays the Rectangle in the form of '#' signs."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updates values of the arguments of the object."""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary representation of Rectangle."""
        return {
                "id" : self.id,
                "width" : self.width,
                "height" : self.height,
                "x" : self.x,
                "y" : self.y
                }

    def __str__(self):
        """String representation of the class Rectangle."""
        return ("[{}] ({}) {}/{} {}/{}".format(self.__class__.__name__, self.id,
            self.x, self.y,
            self.width, self.height))

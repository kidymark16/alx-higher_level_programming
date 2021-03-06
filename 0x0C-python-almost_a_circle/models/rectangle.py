#!/usr/bin/python3
"""Definition of Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a class rectangle.

    Attributes:
        __width: Width of the rectangle
        __height: Height of the rectangle
        __x: x dimen
        __y: y dimen

    Args:
        width: Width of the rectangle
        height: Height of the rectangle
        x: x dimen
        y: y dimen
        id: id of the class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            The width the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            The height the rectangle
        """
        return self.__height

    @property
    def x(self):
        """Gets the x value of the rectangle.
        Returns:
            The x value the rectangle
        """
        return self.__x

    @property
    def y(self):
        """Gets the y value of the rectangle.

        Returns:
            The y value the rectangle
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value: Value to set the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value: Value to set the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x value of the rectangle.
        Args:
            value: Value to set the x of the rectangle
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y value of the rectangle.
        Args:
            value: Value to set the y of the rectangle
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints a diagram of the rectangle using the # symbol."""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Unofficial string representation of the Rectangle class."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the class by assigning argument to each attribute"""
        if len(args) > 0 and args is not None:
            for i in range(len(args)):
                if i is 0:
                    self.id = args[0]
                elif i is 1:
                    self.__width = args[i]
                elif i is 2:
                    self.__height = args[i]
                elif i is 3:
                    self.__x = args[i]
                elif i is 4:
                    self.__y = args[i]
        else:
            for key, value in kwargs.items():
                if key is "id":
                    self.id = value
                elif key is "width":
                    self.__width = value
                elif key is "height":
                    self.__height = value
                elif key is "x":
                    self.__x = value
                elif key is "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns a dictionary representation of the object."""
        dict = {}
        dict.update({'id': self.id, 'width': self.__width,
                     'height': self.__height, 'x': self.__x,
                     'y': self.__y})
        return dict

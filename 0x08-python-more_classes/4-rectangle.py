#!/usr/bin/python3

"""Class that defines a rectangle based on the task 3"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return(0)
        return((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        str = ""
        if self.__width == 0 or self.__height == 0:
            return(str)
        for z in range(0, self.__height):
            for i in range(0, self.__width):
                str = str + '#'
            str = str + '\n'
        str = str[0:-1]
        return(str)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

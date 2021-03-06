#!/usr/bin/python3

""" File with class Square """


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """ __init__ constructor method"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area returns the current square area """
        return self.size ** 2

    def my_print(self):
        """ print square """
        not self.size and print()
        [print(self.size * "#") for _ in range(self.size)]

#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class defines a square with size validation."""

    def __init__(self, size=0):
        """Initialize the square with validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

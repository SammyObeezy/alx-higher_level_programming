#!/usr/bin/python3
"""A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

class Square:
    def __init__(self, size):
        """Initialize a new Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def get_size(self):
         """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    def set_size(self, size):
        """Set the size of the square.

        Args:
            size (int): The new size of the square.
        """
        self.__size = size

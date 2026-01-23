#!/usr/bin/python3
"""
0-add_integer module
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (converted to integers).

    Args:
        a (int/float): first number
        b (int/float): second number, default 98

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

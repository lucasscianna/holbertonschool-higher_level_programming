#!/usr/bin/python3
"""Read UTF8 file to stdout."""


def read_file(filename=""):
    """Read UTF8 file to stdout."""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
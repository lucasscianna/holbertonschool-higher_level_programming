#!/usr/bin/python3
"""Write string to UTF8 file."""


def write_file(filename="", text=""):
    """Write string to UTF8 file, return char count."""
    with open(filename, 'w', encoding="utf-8") as f:
        nb_chars = f.write(text)
    return nb_chars
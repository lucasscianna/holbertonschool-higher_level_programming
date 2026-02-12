#!/usr/bin/python3
"""Append string to UTF8 file."""


def append_write(filename="", text=""):
    """Append string to UTF8 file, return added chars."""
    with open(filename, 'a', encoding="utf-8") as f:
        nb_chars = f.write(text)
    return nb_chars
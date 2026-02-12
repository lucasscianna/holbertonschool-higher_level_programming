#!/usr/bin/python3
"""JSON serialization utility."""


def class_to_json(obj):
    """Returns dict for JSON serialization of obj."""
    return obj.__dict__

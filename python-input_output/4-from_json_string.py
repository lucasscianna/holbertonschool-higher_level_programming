#!/usr/bin/python3
"""Deserialize JSON string to object."""
import json


def from_json_string(my_str):
    """Deserialize JSON string to object."""
    return json.loads(my_str)
#!/usr/bin/python3
"""Serialize object to JSON string."""
import json


def to_json_string(my_obj):
    """Serialize object to JSON string."""
    return json.dumps(my_obj)
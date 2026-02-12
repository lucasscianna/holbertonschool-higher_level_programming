#!/usr/bin/python3
"""JSON dict serialize/deserialize utilities."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize dict to JSON file."""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON file to dict."""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

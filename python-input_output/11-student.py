#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Init with first_name, last_name, age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dict rep for JSON serialization."""
        if attrs is None:
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """Replace public attrs from JSON dict."""
        for key, value in json.items():
            setattr(self, key, value)
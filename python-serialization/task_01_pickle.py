#!/usr/bin/python3
"""CustomObject pickle serialization."""
import pickle


class CustomObject:
    """Custom class with name, age, is_student."""

    def __init__(self, name, age, is_student):
        """Init with name, age, is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize to pickle file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize pickle to CustomObject."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None

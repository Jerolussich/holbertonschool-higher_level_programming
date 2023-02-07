#!/usr/bin/python3
"""shebang"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initializes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            full_dict = self.__dict__
            attrs_dict = {}
            for key in full_dict:
                if key in attrs:
                    attrs_dict[key] = full_dict.get(key)
            return attrs_dict
        return self.__dict__

    def reload_from_json(self, json):
        """change attributes to student instance dict"""
        for key in json:
            setattr(self, key, json.get(key))

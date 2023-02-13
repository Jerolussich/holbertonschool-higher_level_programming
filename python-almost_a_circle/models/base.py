#!/usr/bin/python3
"""base.py"""


import json
import os.path


class Base:

    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initilizes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert class to json"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from json string to object"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """json representation to a file"""
        file = f"{cls.__name__}" + ".json"
        if list_objs is None:
            with open(file, 'w') as file:
                file.write('[]')
            return

        string = "["
        for i, list in enumerate(list_objs):
            if i != 0:
                string += ", "
            string += cls.to_json_string(list.to_dictionary())
        string += "]"

        with open(file, 'w') as file:
            file.write(string)

    @classmethod
    def create(cls, **dictionary):
        """create an instance"""

        name = cls.__name__
        if name == "Square":
            instance = cls(10)
        if name == "Rectangle":
            instance = cls(10, 10)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = cls.__name__ + '.json'

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            file_contents = file.read()
        instances = cls.from_json_string(file_contents)
        list = []
        for dict in instances:
            list.append(cls.create(**dict))
        return list

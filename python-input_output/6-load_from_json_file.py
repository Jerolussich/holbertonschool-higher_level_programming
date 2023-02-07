#!/usr/bin/python3
"""shebang"""


import json
"""import Json"""


def load_from_json_file(filename):
    """turn object from json"""
    with open(filename, "r") as file:
        return json.load(file)

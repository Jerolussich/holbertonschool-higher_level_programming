#!/usr/bin/python3
"""shebang"""

import json


def from_json_string(my_str):
    """convert json to string"""
    return json.loads(my_str)

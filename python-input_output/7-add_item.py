#!/usr/bin/python3
"""shebang"""

import sys
import json
"""import json"""
"""import sys"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
with open(filename, 'r+', encoding="utf-8") as f:
    content = f.read()
    formated_content = content.replace(
        "[", "").replace("]", "").replace(",", "").replace("\"", "").replace(" ", "")

    formated_content = formated_content.split(" ")
    new_list = []
    new_list = formated_content + args[1:]

    save_to_json_file(new_list, filename)
    load_from_json_file(filename)

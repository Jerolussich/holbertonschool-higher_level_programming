#!/usr/bin/python3
"""shebang"""

import json
"""import json"""


def save_to_json_file(my_obj, filename):
    """save json strucutre to file.txt"""

    with open(filename, "w+") as file:
        json.dump(my_obj, file)
        file.close()

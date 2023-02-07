#!/usr/bin/python3
"""shebang"""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """main function"""
    args = sys.argv
    filename = "add_item.json"

    new_list = []

    try:
        with open(filename, 'r', encoding="utf-8") as f:

            if len(f.read()) != 3:

                formated_content = load_from_json_file(filename)
                new_list = formated_content + args[1:]
            else:
                new_list += args[1:]

            save_to_json_file(new_list, filename)

    except FileNotFoundError:
        with open(filename, 'w', encoding="utf-8") as f:

            new_list += args[1:]
            save_to_json_file(new_list, filename)


if __name__ == "__main__":
    main()

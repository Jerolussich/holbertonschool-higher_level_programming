#!/usr/bin/python3
"""shebang"""


class MyList(list):
    """my list class"""

    def print_sorted(self):
        """print sorted list elements"""
        new_list = self[:]
        new_list.sort()
        print(new_list)

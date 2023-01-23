#!/usr/bin/python3


def roman_to_int(roman_string):
    """function def roman_to_int(roman_string): that converts a Roman numeral to an integer"""
    dict_numerals = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dict_exceptions = {"IV": 4, "IX": 9,
                       "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    exceptions_list = dict_exceptions.keys()
    exc_indices = []

    for item in exceptions_list:
        idx = roman_string.find(item)
        if idx != - 1:
            exc_indices.append(idx)

    i = 0
    sum = 0

    while i < len(roman_string):
        if i in exc_indices:
            sum += dict_exceptions[roman_string[i:i+2]]
            i += 1
        else:
            sum += dict_numerals[roman_string[i]]
        i += 1
    return sum

#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """returns a set of all elements present in only one set"""
    new_set = []

    for item_1 in set_1:
        if item_1 not in set_2 and item_1 not in new_set:
            new_set.append(item_1)
    for item_2 in set_2:
        if item_2 not in set_1 and item_2 not in new_set:
            new_set.append(item_2)
    return (new_set)

# This solution occured to me later but the original felt more intutive
#only_in_set_1 = set_1 - set_2
#only_in_set_2 = set_2 - set_1
# only_in_set_1.union(only_in_set_2)

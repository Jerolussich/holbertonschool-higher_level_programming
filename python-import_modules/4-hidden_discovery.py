#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for items in names:
        if (items[:2] != '__'):
            print(items)

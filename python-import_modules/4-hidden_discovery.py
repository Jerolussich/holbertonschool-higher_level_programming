#!/usr/bin/python3


if __name__ == "__main__":
    import hidden_4
    for content in dir(hidden_4):
        if content[:2] != "__":
            print(content)

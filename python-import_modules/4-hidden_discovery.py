#!/usr/bin/python3


if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for content in names:
        if content[0:2] != "__":
            print(content)
    

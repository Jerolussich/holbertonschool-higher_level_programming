#!/usr/bin/python3

def uppercase(str):

    counter = 0

    for letter in str:
        ascii_value = ord(str[counter])

        if ascii_value >= 97 and ascii_value <= 122:
            print("{}".format(chr(ascii_value - 32)), end="")
        else:
            print("{}".format(letter), end="")
        counter += 1
    print("\n")

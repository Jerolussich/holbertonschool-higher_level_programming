#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    counter = 1
    argument_number = len(sys.argv)

    if argument_number == 1:
        print("0 arguments.")
    elif argument_number == 2:
        print("1 argument:\n1: {}".format(sys.argv[counter]))
    elif argument_number > 2:
        print("{} arguments:".format(argument_number - 1))
        for counter in range(1, argument_number):
            print("{}: {}".format(counter, sys.argv[counter]))
            counter += 1
